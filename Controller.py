#!/bin/env python3
import subprocess
import time
from SpeakAndHear import speak
from SpeakAndHear import listen
from SpeakAndHear import convertw2t


# use SpeakAndHear modules to speak text, listen for speech, and convert speech to text.


def __main__():
    speak.speak("What is your name?")
    listen.listen()
    subprocess.call(
        ["sox", "listen.wav", "reversed.wav", "silence", "1", "0.1", "1%", "reverse"]
    )
    subprocess.call(
        ["sox", "reversed.wav", "silenced.wav", "silence", "1", "0.1", "1%", "reverse"]
    )
    subprocess.call(
        ["sox", "silenced.wav", "speech.wav", "noisered", "speech.noiseprofile", "0.3"]
    )
    subprocess.call(["aplay", "speech.wav"])
    text = convertw2t.convertw2t("speech.wav")
    print(text)
    # speak.speak(text)


if __name__ == "__main__":
    __main__()
