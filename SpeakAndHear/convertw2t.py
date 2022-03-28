from vosk import Model, KaldiRecognizer
import gtts
import pyaudio
import wave
import subprocess
import json

# import time
# import os


def convertw2t(file):
    model = Model("model")
    wf = wave.open(file, "rb")
    rec = KaldiRecognizer(model, wf.getframerate())
    rec.SetWords(True)
    text_lst = []
    p_text_lst = []
    p_str = []
    len_p_str = []
    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            text_lst.append(rec.Result())
            print(rec.Result())
        else:
            p_text_lst.append(rec.PartialResult())
            print(rec.PartialResult())

    if len(text_lst) != 0:
        jd = json.loads(text_lst[0])
        txt_str = jd["text"]

    elif len(p_text_lst) != 0:
        for i in range(0, len(p_text_lst)):
            temp_txt_dict = json.loads(p_text_lst[i])
            p_str.append(temp_txt_dict["partial"])

        len_p_str = [len(p_str[j]) for j in range(0, len(p_str))]
        max_val = max(len_p_str)
        indx = len_p_str.index(max_val)
        txt_str = p_str[indx]

    else:
        txt_str = ""

    return txt_str
