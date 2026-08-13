import io
import os
import sys
import asyncio
import edge_tts

# Ep Windows Console dung UTF-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', line_buffering=True)
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', line_buffering=True)

from flask import Flask, request, jsonify, Response
from flask_cors import CORS

PORT = 5000
HOST = '0.0.0.0'
DEFAULT_VOICE = "vi-VN-HoaiMyNeural" # ban co the thay doi thanh vi-VN-NamMinhNeural neu muon giong nam

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*", "allow_headers": ["Content-Type", "ngrok-skip-browser-warning", "X-Pinggy-No-Screen", "Bypass-Tunnel-Reminder"]}})

print("Dang khoi tao may chu MS Edge TTS...")
print(f"-> Giong doc mac dinh: {DEFAULT_VOICE}")
print(f"-> May chu am thanh da san sang tai: http://localhost:{PORT}")

@app.route('/')
def index():
    return f"<h1>✅ May chu MS Edge TTS dang hoat dong tot!</h1><p>Giong doc: {DEFAULT_VOICE}</p><p>Vui long mo file sender.html de su dung.</p>"

async def get_audio_bytes(text, voice, rate="+0%"):
    communicate = edge_tts.Communicate(text, voice, rate=rate)
    audio_data = b""
    async for chunk in communicate.stream():
        if chunk["type"] == "audio":
            audio_data += chunk["data"]
    return audio_data

@app.route('/tts', methods=['GET', 'POST'])
def generate_tts():
    text = request.args.get('text')
    if not text:
        return jsonify({"error": "Thieu tham so 'text'"}), 400

    # Tuy chon giong doc qua tham so truyen vao, hoac dung mac dinh
    voice = request.args.get('voice', DEFAULT_VOICE)
    # Tuy chon toc do (vi du: +10%, -10%, hoac +0%)
    rate = request.args.get('rate', '+0%')

    print(f"\n[+] Yeu cau doc: '{text}' (Voice: {voice}, Rate: {rate})")
    
    try:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        audio_data = loop.run_until_complete(get_audio_bytes(text, voice, rate))
        loop.close()
        
        # Edge TTS tra ve file MP3
        return Response(audio_data, mimetype="audio/mpeg")
    except Exception as e:
        print(f"Loi tao audio: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host=HOST, port=PORT, threaded=True)
