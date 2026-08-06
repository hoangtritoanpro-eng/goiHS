import pocket_tts
import sys
import numpy as np
import torch

tts_model = pocket_tts.TTSModel.load_model()
voice_state = tts_model.get_state_for_audio_prompt("alba")

print("Model loaded")
stream = tts_model.generate_audio_stream(voice_state, "Hello world")
for chunk in stream:
    print(type(chunk))
    if isinstance(chunk, torch.Tensor):
        print(chunk.shape, chunk.dtype)
    break
