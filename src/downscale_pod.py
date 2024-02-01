import moviepy.editor as mp


class DownscalePod:
    def __init__(self, video_path: str) -> None:
        self.video_path = video_path
        self.video = mp.VideoFileClip(self.video_path)
    
    def downscale(self, height: int, filename: str) -> None:
        clip_resized = self.video.resize(height=height)
        clip_resized.write_videofile(filename)

downpod1 = DownscalePod("ressources\\mp4\\video.mp4")
downpod1.downscale(360, "ressources\\mp4\\video_resized.mp4")

downpod2 = DownscalePod("ressources\\mp4\\video_2.mp4")
downpod2.downscale(360, "ressources\\mp4\\video_2_resized.mp4")
