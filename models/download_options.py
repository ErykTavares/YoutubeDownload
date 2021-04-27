from pytube import YouTube


class Download():
    def __init__(self, url, path, bar, porcent):
        self.url = url
        self.path = path
        self.bar = bar
        self.porcent = porcent

    def progress_funct(self, chunk, file_handle, bytes_remaning):
        size = chunk.filesize
        download = size - bytes_remaning
        progress = download / size * 100
        porcent = str(int(progress)) + "%"
        return self.bar.UpdateBar(progress), self.porcent.update(porcent)


    def video_download(self):
        """Faz o download do video"""
        youtube = YouTube(self.url, on_progress_callback=self.progress_funct).streams.get_highest_resolution().download(self.path)

    def mp3_download(self):
        """Faz o download somente do audio do video"""
        youtube = YouTube(self.url, on_progress_callback=self.progress_funct).streams.get_audio_only().download(self.path, filename_prefix=".mp3")


# copyright ErykTavares © 2021



#video_download("https://www.youtube.com/watch?v=vv81LmZ9Wog", r"Desafio85\\download")