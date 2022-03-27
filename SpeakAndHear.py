#!/bin/env python3

# use vosk and gTTS to speak and hear


def speakAndHear(text):
    import os
    import vosk
    import gtts
    import time
    import pyaudio
    import wave
    import sys
    import subprocess

    # create a speech synthesizer
    vo = vosk.Model("model/en-us/en-us")

    def speak():
        # convert text to speech
        tts = gtts.gTTS(text, lang="en")
        tts.save("speak.mp3")
        # play the speech
        subprocess.call(["mpg321", "speak.mp3"])
