import time
import requests

start = time.time()
print("Sending request...")
response = requests.get("http://localhost:5000/tts?text=Xin%20ch%C3%A0o%20c%C3%A1c%20b%E1%BA%A1n%20h%E1%BB%8Dc%20sinh", stream=True)
content = response.content
print(f"Total time elapsed for full download: {time.time() - start:.2f} seconds")
print(f"Total size: {len(content)} bytes")
