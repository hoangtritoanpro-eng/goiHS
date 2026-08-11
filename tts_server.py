import io
import os
import sys
import wave
import numpy as np

# Ep Windows Console dung UTF-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', line_buffering=True)
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', line_buffering=True)

from flask import Flask, request, jsonify, Response
from flask_cors import CORS

PORT = 5000
HOST = '0.0.0.0'
CUSTOM_VOICE_FILE = "y_custom_voice.mp3"
CUSTOM_VOICE_NAME = "giao_vien_custom"

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*", "allow_headers": ["Content-Type", "ngrok-skip-browser-warning", "X-Pinggy-No-Screen", "Bypass-Tunnel-Reminder"]}})

print("Dang khoi tao mo hinh VieNeu-TTS... Vui long doi trong giay lat.")
try:
    from vieneu import Vieneu
    # backend="onnx" ep chay CPU int8 streaming tot nhat
    vieneu_model = Vieneu(backend="onnx")
    
    if os.path.exists(CUSTOM_VOICE_FILE):
        print(f"Phat hien file giong mau: {CUSTOM_VOICE_FILE}. Dang tien hanh Clone giong...")
        vieneu_model.add_voice(CUSTOM_VOICE_NAME, CUSTOM_VOICE_FILE, denoise=True)
        print("[OK] Da san sang giong Clone!")
    else:
        print(f"[WARNING] Khong tim thay file '{CUSTOM_VOICE_FILE}'.")

    print(f"-> May chu Am thanh AI da san sang tai: http://localhost:{PORT}")
except Exception as e:
    print(f"[ERROR] Loi khoi tao Mo hinh: {e}")
    sys.exit(1)


@app.route('/')
def index():
    return "<h1>✅ May chu AI Voice Cloning dang hoat dong tot!</h1><p>Vui long mo file sender.html de su dung.</p>"

def _pcm16(audio_f32: np.ndarray) -> bytes:
    return (np.asarray(audio_f32) * 32767).clip(-32768, 32767).astype(np.int16).tobytes()

@app.route('/tts', methods=['GET', 'POST'])
def generate_tts():
    text = request.args.get('text')
    if not text:
        return jsonify({"error": "Thieu tham so 'text'"}), 400

    print(f"\\n[+] Yeu cau doc (Full): '{text}'")
    
    try:
        voice_to_use = CUSTOM_VOICE_NAME if os.path.exists(CUSTOM_VOICE_FILE) else None
        audio_array = vieneu_model.infer(text, voice=voice_to_use, speed=0.8)
        
        # Chuyen numpy array sang WAV in-memory
        h = io.BytesIO()
        with wave.open(h, "wb") as w:
            w.setnchannels(1)
            w.setsampwidth(2)
            w.setframerate(48000)
            pcm_bytes = _pcm16(audio_array)
            w.writeframes(pcm_bytes)
            
        return Response(h.getvalue(), mimetype="audio/wav")
    except Exception as e:
        print(f"Loi tao audio: {e}")
        return jsonify({"error": str(e)}), 500

@app.route('/tts_raw', methods=['GET', 'POST'])
def generate_tts_raw():
    text = request.args.get('text')
    if not text:
        return jsonify({"error": "Thieu tham so 'text'"}), 400

    print(f"\\n[+] Yeu cau doc (Raw Streaming): '{text}'")
    
    def gen():
        try:
            voice_to_use = CUSTOM_VOICE_NAME if os.path.exists(CUSTOM_VOICE_FILE) else None
            for chunk in vieneu_model.infer_stream(text, voice=voice_to_use, speed=0.8):
                if chunk is not None and len(chunk) > 0:
                    yield _pcm16(chunk)
        except Exception as e:
            print(f"Loi streaming raw audio: {e}")

    return Response(gen(), mimetype="application/octet-stream")

if __name__ == '__main__':
    # Chay bang process thuong cua Flask (voi debug off) ho tro generator
    app.run(host=HOST, port=PORT, threaded=True)
