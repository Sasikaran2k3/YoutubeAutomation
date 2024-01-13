import torch
from TTS.api import TTS
import os
import datetime

date = "".join(str(datetime.date.today()).split("-"))
f = open(os.path.dirname(__file__) + "//Data//" + date + "_script.txt", "r")
content = f.read()

stripped_content = content + ".Stay updated by following Entertain Buddy, hit like, and drop 'buddy' in the comments for more details!"

print(stripped_content)

tts = TTS(model_name="tts_models/multilingual/multi-dataset/xtts_v2", progress_bar=False)
path = f"{os.path.dirname(__file__)}/Data/{date}.wav"
tts.tts_to_file(text=stripped_content, file_path=path,language='en',speaker_wav=os.path.dirname(__file__)+"/Audio_train.wav")
