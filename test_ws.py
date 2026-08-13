import asyncio
import websockets

async def test_ws():
    uri = "wss://speech.platform.bing.com/consumer/speech/synthesize/readaloud/edge/v1?TrustedClientToken=6A5AA1D4EAFF4E9FB37E23D68491D6F4"
    headers = {
        "Origin": "http://localhost:8080",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203"
    }
    try:
        async with websockets.connect(uri, additional_headers=headers) as ws:
            print("Connected successfully!")
            await ws.close()
    except Exception as e:
        print(f"Failed to connect: {e}")

asyncio.run(test_ws())
