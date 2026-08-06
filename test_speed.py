import time
from vieneu import Vieneu

print("Loading model...")
vieneu_model = Vieneu(backend="onnx")

text = "Mời bạn Nguyễn Ngọc Châu Anh bảy năm, phụ huynh đón về."
print(f"Testing infer_stream...")
start = time.time()
chunks = list(vieneu_model.infer_stream(text))
print(f"infer_stream took: {time.time() - start:.2f} seconds")

print(f"Testing infer...")
start = time.time()
audio = vieneu_model.infer(text)
print(f"infer took: {time.time() - start:.2f} seconds")
