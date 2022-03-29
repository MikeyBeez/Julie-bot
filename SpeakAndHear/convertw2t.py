from vosk import Model, KaldiRecognizer, SetLogLevel
import asyncio
import websockets
import sys
import os
import wave
import subprocess


def convertw2t(file):
    SetLogLevel(0)


async def run_test(uri):
    async with websockets.connect(uri) as websocket:
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
            print(await websocket.recv())

        await websocket.send('{"eof" : 1}')
        print("wsr")
        print(await websocket.recv())


asyncio.get_event_loop().run_until_complete(run_test("ws://localhost:2700"))
