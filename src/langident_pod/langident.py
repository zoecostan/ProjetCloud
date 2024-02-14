from langdetect import detect
from typing import Optional

import moviepy.editor as mp
import speech_recognition as sr
import os
import time

class AudioPod:
    def __init__(self, video_path: Optional[str], audio_path: Optional[str]) -> None:
        if video_path:
            video = mp.VideoFileClip(video_path)
            audio = video.audio
            audio.write_audiofile(audio_path)
            self.audio_path = audio_path
        else:
            self.audio_path = audio_path

    def transcribe_audio(self) -> str:
        r = sr.Recognizer()

        with sr.AudioFile(self.audio_path) as source:
            r.adjust_for_ambient_noise(source)
            data = r.record(source)
            text = r.recognize_whisper(data)
        
        return text
    
    def get_lang(self, metadata_filename: str) -> str:
        lang = detect(self.transcribe_audio())
        with open(metadata_filename, "a") as f:
            f.write(f"Fichier audio : {self.audio_path}\n")
            f.write(f"Langage : {lang}")
        with open("/app/tmp/langident_finish.txt", "w") as indicator_file:
            indicator_file.write("Langident finished.")
        return lang


video_path = "/app/results/video1_resized.mp4"
audio_path = "/app/results/video1_audio.wav"
metadata_path = "/app/results/metadata1.txt"

#wait for the video to be released
while not os.path.exists("/app/tmp/downscale_finish.txt"):
    time.sleep(1)

#delete the file if it exists
os.remove("/app/tmp/downscale_finish.txt")

audpod1 = AudioPod(video_path, audio_path)
lang1 = audpod1.get_lang(metadata_path)