import wave
import sys
import json
from vosk import Model, KaldiRecognizer, SetLogLevel
from pydub import AudioSegment
import os
from llama_index.llms.ollama import Ollama
from pydub import AudioSegment

# Exécute le projet sur GPU plutôt que CPU
os.environ["CUDA_VISIBLE_DEVICES"] = "0"

# Transformer le fichier en bon format mono PCM
sound = AudioSegment.from_wav(sys.argv[1])
sound = sound.set_channels(1)
sound.export(sys.argv[1], format="wav")

# Obtenir les logs du modèle vost
SetLogLevel(0)

# Parametrage
wf = wave.open(sys.argv[1], "rb")
if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
    print("Audio file must be WAV format mono PCM.")
    sys.exit(1)

model_name = "vosk-model-fr-0.6-linto-2.2.0"
model = Model(model_name)

rec = KaldiRecognizer(model, wf.getframerate())
rec.SetWords(True)
rec.SetPartialWords(True)

# On créer le fichier transcripte et on y écrit ce que le modèle nous renvoie comme résultat
with open("result/transcription.txt", "w", encoding='utf-8') as transcription_file:
    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            result_json = json.loads(rec.Result())
            transcription = result_json["text"] + "\n"
            transcription_file.write(transcription)

# On récupère l'ensemble du transcript pour le prompt
file_path = "result/transcription.txt"
with open(file_path, "r", encoding="utf-8") as file:
    file_contents = file.read()

prompt = ("Présente l'auteur du transcript en français et de quoi es ce qu'il parle (20 mots maximum), ne réecris "
          "surtout pas le transcript : " + '"' +
          file_contents + '"')

# On demande au LLM de nous générer une description avec le prompt au dessus
llm = Ollama(model="mistral", request_timeout=50.0)
result = llm.complete(prompt)

with open("result/description.txt", "w", encoding='utf-8') as description_file:
    description_file.write(result.text.strip())
