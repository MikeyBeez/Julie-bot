#!/bin/env python3
from json import tool
import subprocess
import time
from SpeakAndHear import speak
from SpeakAndHear import listen
from SpeakAndHear import convert
from Tools import clean


def __main__():
    speak.speak("What is your name?")
    listen.listen(3)
    subprocess.call(
        ["sox", "listen.wav", "reversed.wav", "silence", "1", "0.1", "1%", "reverse"]
    )
    subprocess.call(
        ["sox", "reversed.wav", "silenced.wav", "silence", "1", "0.1", "1%", "reverse"]
    )
    subprocess.call(
        ["sox", "silenced.wav", "speech.wav", "noisered", "speech.noiseprofile", "0.3"]
    )
    result = convert.convert("speech.wave")
    # print("The final text is: ")
    # print(result)
    clean.clean()


if __name__ == "__main__":
    __main__()
