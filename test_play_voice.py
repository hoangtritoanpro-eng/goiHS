import os
import time
import wave
import numpy as np

import sys
import io

# Force Windows Console to use UTF-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

print("Đang tải AI Voice Model... Vui lòng đợi...")
from vieneu import Vieneu
# Sử dụng backend y hệt tts_server.py
vieneu_model = Vieneu(backend="onnx")

CUSTOM_VOICE_FILE = "y_custom_voice.mp3"
CUSTOM_VOICE_NAME = "giao_vien_custom"

if os.path.exists(CUSTOM_VOICE_FILE):
    print(f"Đang Clone giọng từ file {CUSTOM_VOICE_FILE}...")
    vieneu_model.add_voice(CUSTOM_VOICE_NAME, CUSTOM_VOICE_FILE, denoise=True)
else:
    print(f"Lỗi: Không tìm thấy file {CUSTOM_VOICE_FILE}")
    exit(1)

text = "Chào bạn, hệ thống đã được khôi phục thành công về đầu ngày hôm nay. Đây là bài kiểm tra giọng đọc cô giáo."
print(f"Đang tạo giọng đọc cho câu: '{text}'")
audio_array = vieneu_model.infer(text, voice=CUSTOM_VOICE_NAME)

def _pcm16(audio_f32: np.ndarray) -> bytes:
    return (np.asarray(audio_f32) * 32767).clip(-32768, 32767).astype(np.int16).tobytes()

wav_file = "test_custom_output.wav"
with wave.open(wav_file, "wb") as w:
    w.setnchannels(1)
    w.setsampwidth(2)
    w.setframerate(48000)
    w.writeframes(_pcm16(audio_array))

print(f"Đã lưu thành công ra {wav_file}. Đang phát âm thanh trên máy của bạn...")
# Mở file wav bằng trình phát nhạc mặc định của Windows
os.startfile(wav_file)
