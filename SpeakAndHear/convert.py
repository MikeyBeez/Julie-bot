import asyncio
from re import A
import websockets
import sys
import wave


async def run_test(uri):
    async with websockets.connect(uri) as websocket:  # type: ignore

        filetoopen = "speech.wav"
        wf = wave.open(filetoopen, "rb")
        await websocket.send(
            '{ "config" : { "sample_rate" : %d } }' % (wf.getframerate())
        )
        buffer_size = int(wf.getframerate() * 0.1)  # 0.2 seconds of audio
        while True:
            data = wf.readframes(buffer_size)

            if len(data) == 0:
                break

            await websocket.send(data)
            rcvstr = print(await websocket.recv())
            print("rcvstr")

        await websocket.send('{"eof" : 1}')
        rcvstr2 = print(await websocket.recv())
        return rcvstr2
        print("rcvstr2")


def convert(file):
    asyncio.get_event_loop().run_until_complete(run_test("ws://localhost:2700"))
