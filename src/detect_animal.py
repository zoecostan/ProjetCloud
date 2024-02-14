import subprocess
import json
from moviepy.editor import VideoFileClip
import shutil
import os

def generate_video_with_audio():
    # Commande à exécuter pour générer la vidéo sans audio
    command = [
        "python",
        "./yolov5/detect.py",
        "--weights", "./yolov5/runs/train/exp/weights/last.pt",
        "--img", "640",
        "--conf", "0.6",
        "--source", "./ressources/Capybara.mp4"
    ]
    subprocess.run(command)

    # Chemin vers la vidéo générée
    video_generee_path = "./yolov5/runs/detect/exp/Capybara.mp4"

    # Charger la vidéo générée
    video_generee = VideoFileClip(video_generee_path)

    # Charger la vidéo d'origine
    video_origine = VideoFileClip("./ressources/Capybara.mp4")

    # Extraire et ajouter l'audio de la vidéo d'origine à la vidéo générée
    video_generee = video_generee.set_audio(video_origine.audio)

    # Sauvegarder la vidéo finale
    video_generee.write_videofile("video_detection.mp4")

    # Fermer les clips vidéo
    video_generee.close()
    video_origine.close()

    # Supprimer le dossier et son contenu
    shutil.rmtree("./yolov5/runs/detect/exp")

    # Supprimer le fichier de logs
    os.remove("logs.txt")

# Analyser les logs pour extraire les animaux détectés
log_file_path = "./logs.txt"
detected_animals = set()  # Utiliser un ensemble pour éviter les doublons

with open(log_file_path, "r") as log_file:
    for line in log_file:
        if "chat" in line.lower():
            detected_animals.add("chat")
        if "capybara" in line.lower():
            detected_animals.add("capybara")
        if "leopard" in line.lower():
            detected_animals.add("leopard")

# Créer le contenu du fichier JSON si au moins une des trois espèces est détectée
if detected_animals:
    data = {
        "Animaux": list(detected_animals)
    }

    # Chemin vers le fichier JSON généré
    json_file_path = "detected_animals.json"

    # Enregistrer les données dans le fichier JSON
    with open(json_file_path, "w") as json_file:
        json.dump(data, json_file, indent=6, separators=(",", ": "))

# Appeler la fonction pour générer la vidéo avec l'audio
generate_video_with_audio()
