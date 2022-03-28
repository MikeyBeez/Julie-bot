from vosk import Model, KaldiRecognizer, SetLogLevel
import sys
import os
import wave
import subprocess


def convertw2t(file):
    SetLogLevel(0)
    model = Model("model")
    wf = wave.open(file, "rb")
    rec = KaldiRecognizer(model, wf.getframerate())
    sample_rate = wf.getframerate()

    process = subprocess.Popen(
        [
            "ffmpeg",
            "-loglevel",
            "quiet",
            "-i",
            "speech.wav",
            "ar",
            str(sample_rate),
            "-ac",
            "1",
            "-f",
            "s16le",
            "-",
        ],
        stdout=subprocess.PIPE,
    )

    while True:
        data = process.stdout.read(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            print(rec.Result())
        else:
            print(rec.PartialResult())
    print(rec.FinalResult())
    return rec.FinalResult()
