from langdetect import detect
from typing import Optional

import moviepy.editor as mp
import speech_recognition as sr


class AudioPod:
    def __init__(self, video_path: Optional[str], audio_filename: Optional[str], audio_path: Optional[str]) -> None:
        if video_path:
            video = mp.VideoFileClip(video_path)
            audio = video.audio
            audio.write_audiofile(audio_filename)
            self.audio_path = audio_filename
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
        return lang
    

audpod1 = AudioPod("ressources\\mp4\\video.mp4", "ressources\\wav\\video_audio.wav", None)
lang1 = audpod1.get_lang("ressources\\txt\\metadata1.txt")

audpod2 = AudioPod("ressources\\mp4\\video_2.mp4", "ressources\\wav\\video_2_audio.wav", None)
lang2 = audpod2.get_lang("ressources\\txt\\metadata2.txt")

audpod3 = AudioPod(None, None, "ressources\\wav\\7601-291468-0006.wav")
lang3 = audpod3.get_lang("ressources\\txt\\metadata3.txt")
