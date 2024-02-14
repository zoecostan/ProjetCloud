import subprocess
import json
from moviepy.editor import VideoFileClip
import shutil
import os
import time

def generate_video_with_audio(video_path, video_detection_path):
    # Commande à exécuter pour générer la vidéo sans audio
    command = [
        "python",                    # Exécuter le programme Python
        "/app/yolov5/detect.py",                 # Nom du script à exécuter
        "--weights", "/app/yolov5/runs/train/exp/weights/last.pt",  # Argument --weights avec le chemin du fichier poids
        "--img", "640",              # Argument --img avec la valeur 640
        "--conf", "0.6",             # Argument --conf avec la valeur 0.5
        "--source", "${video_path}"  # Argument --source avec le chemin du fichier vidéo source
    ]

    # Exécution de la commande pour générer la vidéo sans audio
    subprocess.run(command)

    # Chemin vers le dossier contenant la vidéo générée
    video_folder_path = "/app/yolov5/runs/detect/exp"

    # Chemin vers la vidéo générée
    video_generee_path = video_folder_path + "/video.mp4"

    # Charger la vidéo générée
    video_generee = VideoFileClip(video_generee_path)

    # Charger la vidéo d'origine
    video_origine = VideoFileClip(video_path)

    # Extraire l'audio de la vidéo d'origine
    audio_origine = video_origine.audio

    # Ajouter l'audio de la vidéo d'origine à la vidéo générée
    video_generee = video_generee.set_audio(audio_origine)

    # Sauvegarder la vidéo finale
    video_generee.write_videofile(video_detection_path)

    # Fermer les clips vidéo
    video_generee.close()
    video_origine.close()

    # Supprimer le dossier et son contenu
    shutil.rmtree(video_folder_path)


#wait for the video to be released
while not os.path.exists("/app/tmp/subtitle_finish.txt"):
    time.sleep(1)

#delete the file if it exists
os.remove("/app/tmp/subtitle_finish.txt")

# Analyser les logs pour extraire les animaux détectés
log_file_path = "/app/tmp/logs.txt"
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


# Supprimer le fichier de logs
os.remove(log_file_path)

# Appeler la fonction pour générer la vidéo avec l'audio
video_path = "/app/results/video1_subtitled.mp4"
video_detection_path = "/app/results/video1_detection.mp4"
generate_video_with_audio(video_path, video_detection_path)
with open("/app/tmp/animalDetect_finish.txt", "w") as indicator_file:
    indicator_file.write("AnimalDetect finished.")
