# use vosk and gTTS to speak and hear
# Make sure that you have installed pyaudio, vosk, and gTTS.
# conda install pyaudio
# pip3 install vosk
# pip3 install gtts


import os
import vosk
import gtts
import time
import pyaudio
import wave
import subprocess

# function to convert wave file to text using vosk

def convertToText():
# convert the wave file to text
# create a speech synthesizer
    vo = vosk.Model("model/en-us/en-us")
    text = vo.Text("wb.wav")
    return text

        