import subprocess
from moviepy.editor import VideoFileClip
import shutil

def generate_video_with_audio():
    # Commande à exécuter pour générer la vidéo sans audio
    command = [
        "python",                    # Exécuter le programme Python
        "../yolov5/detect.py",                 # Nom du script à exécuter
        "--weights", "../yolov5/runs/train/exp/weights/last.pt",  # Argument --weights avec le chemin du fichier poids
        "--img", "640",              # Argument --img avec la valeur 640
        "--conf", "0.6",             # Argument --conf avec la valeur 0.5
        "--source", "../ressources/Capybara.mp4"  # Argument --source avec le chemin du fichier vidéo source
    ]

    # Exécution de la commande pour générer la vidéo sans audio
    subprocess.run(command)

    # Chemin vers le dossier contenant la vidéo générée
    video_folder_path = "../yolov5/runs/detect/exp"

    # Chemin vers la vidéo générée
    video_generee_path = video_folder_path + "/Capybara.mp4"

    # Charger la vidéo générée
    video_generee = VideoFileClip(video_generee_path)

    # Charger la vidéo d'origine
    video_origine = VideoFileClip("../ressources/Capybara.mp4")

    # Extraire l'audio de la vidéo d'origine
    audio_origine = video_origine.audio

    # Ajouter l'audio de la vidéo d'origine à la vidéo générée
    video_generee = video_generee.set_audio(audio_origine)

    # Sauvegarder la vidéo finale
    video_generee.write_videofile("video_detection.mp4")

    # Fermer les clips vidéo
    video_generee.close()
    video_origine.close()

    # Supprimer le dossier et son contenu
    shutil.rmtree(video_folder_path)

# Appeler la fonction pour générer la vidéo avec l'audio
generate_video_with_audio()
