import asyncio
import edge_tts

async def get_audio_bytes(text, voice):
    communicate = edge_tts.Communicate(text, voice)
    audio_data = b""
    async for chunk in communicate.stream():
        if chunk["type"] == "audio":
            audio_data += chunk["data"]
    return audio_data

def main():
    text = "Xin chào, học sinh Nguyễn Văn A lớp 6/1 đã về."
    voice = "vi-VN-HoaiMyNeural"
    audio = asyncio.run(get_audio_bytes(text, voice))
    with open("test_edge_output.mp3", "wb") as f:
        f.write(audio)
    print("Done! Wrote to test_edge_output.mp3")

if __name__ == "__main__":
    main()
