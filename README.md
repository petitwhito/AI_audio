# Projet Audio AI

Ce projet consiste à prendre un épisode de podcast en entrée (au format .wav ou .mp3) et à générer automatiquement le transcript et la description dans le dossier "result".

## Installation

Pour installer les dépendances nécessaires, exécutez la commande suivante :

```
pip3 install -r requirements.txt
```

De plus, assurez-vous de télécharger Ollama depuis le lien suivant : [https://github.com/ollama/ollama](https://github.com/ollama/ollama) \
Et de télécharger le modèle vost FR (vosk-model-fr-0.22) depuis le lien suivant :
 [https://alphacephei.com/vosk/models/vosk-model-fr-0.22.zip](https://alphacephei.com/vosk/models/vosk-model-fr-0.22.zip)

## Utilisation

Pour lancer le programme, exécutez la commande suivante en remplaçant `[path du fichier audio]` par le chemin vers votre fichier audio en format .WAV:

```
python3 main.py [path du fichier audio]
```
## Détails techniques

Ce projet utilise Ollama comme LLM (Large Language Model) et le modèle Vosk pour la transcription automatique. Le code est commenté pour fournir des informations supplémentaires (comme le prompt) si nécessaire.
