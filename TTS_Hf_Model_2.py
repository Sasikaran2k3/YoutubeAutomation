import torch
from TTS.api import TTS
import os
import datetime

date = "".join(str(datetime.date.today()).split("-"))
f = open(os.path.dirname(__file__) + "//Data//" + date + "_script.txt", "r")
content = f.readlines()
stripped_content = ""
for i in content:
    stripped_content += i.strip() + "\n"
    stripped_content = stripped_content
#tts = TTS(model_name="tts_models/multilingual/multi-dataset/xtts_v2", progress_bar=False)
tts = TTS(model_name="tts_models/en/vctk/vits", progress_bar=False)
path = f"{os.path.dirname(__file__)}/Data/{date}.wav"

tts.tts_to_file(text=stripped_content, file_path=path,speaker="p302")