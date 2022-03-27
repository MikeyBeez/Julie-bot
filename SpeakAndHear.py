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

    def listen():
        # listen for speech
        CHUNK = 1024
        FORMAT = pyaudio.paInt16
        CHANNELS = 1
        RATE = 16000
        RECORD_SECONDS = 3
        WAVE_OUTPUT_FILENAME = "listen.wav"

        p = pyaudio.PyAudio()

        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)

        print("* recording")

        frames = []

        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)

        print("* done recording")

        stream.stop_stream()
        stream.close()
        p.terminate()

        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()

    def recognize():
        # recognize speech
        vo.SetKey('voice', 'native')
        text = vo.OralProcess(WAVE_OUTPUT_FILENAME)
        return text

        