from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

import datetime
import pyaudio
import pysrt
import speech_recognition as sr


class SubtitlePod:
    def __init__(self, video_path: str, audio_path: str) -> None:
        self.video_path = video_path
        self.video = VideoFileClip(video_path)
        self.audio_path = audio_path
        self.srt_path = None
        self.srt_block_num = 1

    def set_srt_path(self, filename: str) -> None:
        self.srt_path = filename

    def speech_to_srt(self, current_time: datetime.datetime, block_num: int):
        r = sr.Recognizer()
        with sr.AudioFile(self.audio_path) as source:
            if current_time + datetime.timedelta(seconds=4) < datetime.datetime.fromtimestamp(self.video.duration) - datetime.timedelta(hours=1):
                r.adjust_for_ambient_noise(source)
                offset = current_time.minute*60 + current_time.second + current_time.microsecond/1000000
                print(str(current_time + datetime.timedelta(seconds=4)) + " -- " + str(datetime.datetime.fromtimestamp(self.video.duration)))
                data = r.record(source, duration=4, offset=offset)
                try:
                    text = r.recognize_whisper(data)
                except sr.UnknownValueError:
                    print("Audio error")
                except sr.RequestError:
                    print("Request error")
            elif current_time < datetime.datetime.fromtimestamp(self.video.duration) - datetime.timedelta(hours=1):
                r.adjust_for_ambient_noise(source)
                offset = current_time.minute*60 + current_time.second + current_time.microsecond/1000000
                print(str(current_time) + " --- " + str(datetime.datetime.fromtimestamp(self.video.duration)))
                data = r.record(source, offset=offset)
                try:
                    text = r.recognize_whisper(data)
                except sr.UnknownValueError:
                    print("Audio error")
                except sr.RequestError:
                    print("Request error")
            else:
                return None

        end_time = current_time + datetime.timedelta(seconds=4)

        str_current_time = str(current_time.time())
        str_end_time = str(end_time.time())

        with open(self.srt_path, "a") as f:
            f.write(str(block_num))
            f.write("\n")
            f.write(str_current_time)
            f.write("-->")
            f.write(str_end_time)
            f.write("\n")
            f.write(text)
            f.write("\n")
            f.write("\n")

        return self.speech_to_srt(end_time, block_num + 1)
    
    def create_subtitles(self, srt_filename: str, vid_filename: str) -> None:
        self.set_srt_path(srt_filename)
        self.speech_to_srt(datetime.datetime(1970, 1, 1, 0, 0, 0), self.srt_block_num)

subtitle_pod1 = SubtitlePod("ressources\\mp4\\video_resized.mp4", "ressources\\wav\\video_audio.wav")
subtitle_pod1.create_subtitles("ressources\\txt\\video_subtitles.srt", "ressources\\mp4\\video_subtitled.mp4")
