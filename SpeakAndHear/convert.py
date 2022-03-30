import asyncio
from re import A
import websockets
import sys
import wave
import json

global rcvstr


async def run_test(uri):
    async with websockets.connect(uri) as websocket:  # type: ignore

        filetoopen = "speech.wav"
        wf = wave.open(filetoopen, "rb")
        await websocket.send(
            '{ "config" : { "sample_rate" : %d } }' % (wf.getframerate())
        )
        buffer_size = int(wf.getframerate() * 0.2)  # 0.2 seconds of audio
        while True:
            data = wf.readframes(buffer_size)

            if len(data) == 0:
                break

            await websocket.send(data)
            await websocket.recv()

        await websocket.send('{"eof" : 1}')
        dumped = await websocket.recv()
        print(dumped)
        mydict = json.loads(dumped)
        print(mydict["text"])
        # result = mydict["text"]
        # return result


def convert(file):
    asyncio.get_event_loop().run_until_complete(run_test("ws://localhost:2700"))
