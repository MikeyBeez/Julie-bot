# use vosk and gTTS to speak and hear
# Make sure that you have installed pyaudio, vosk, and gTTS.
# conda install pyaudio
# pip3 install vosk
# pip3 install gtts

import os
import gtts
import pyaudio
import subprocess


def speak(text):
# convert text to speech
    tts = gtts.gTTS(text, lang="en")
    tts.save("speak.mp3")
    # play the speech
    subprocess.call(["mpg321", "speak.mp3"])

        