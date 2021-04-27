import PySimpleGUI as sg
from models.download_options import Download


class Window():
    def __init__(self):
        sg.theme("reddit")
        self.layout = [[sg.Text("Url do video", font="Verdanabold")],
                       [sg.Input(font="Verdanabold", key="-input-", size=(33, 0))],
                       [sg.Button("Download do video", font="Verdanabold"), sg.Button("Download do audio", font="Verdanabold")],
                       [sg.ProgressBar(100, orientation="h", size=(27.6, 30), key="-download_bar-"), sg.Text(size=(5, 0), font="Verdanabold" , text_color="Blue", key="-%-")]

                        ]
        self.window = sg.Window("Youtube Video download", finalize=True).layout(self.layout)
        self.progress_bar = self.window["-download_bar-"]
        self.porcent = self.window["-%-"]

        while True:
            self.event, self.values = self.window.read()
            if self.event == sg.WIN_CLOSED:
                break
            if self.event == "Download do video":
                folder = r"" + sg.popup_get_folder("Salvar onde", font="Verdanabold")
                download = Download(self.values["-input-"], folder, self.progress_bar, self.porcent)
                download.video_download()
                sg.popup("Download completo", font="Verdanabold", auto_close_duration=10000)
                self.window["-download_bar-"].update(0)
                self.window["-%-"].update("")
            
            if self.event == "Download do audio":
                folder = r"" + sg.popup_get_folder("Salvar onde", font="Verdanabold")
                download = Download(self.values["-input-"], folder, self.progress_bar, self.porcent)
                download.mp3_download()
                sg.popup("Download completo", font="Verdanabold", auto_close_duration=10000)
                self.window["-download_bar-"].update(0)
                self.window["-%-"].update("")
        
        self.window.close()


video_and_audio_donwload = Window()

# copyright ErykTavares © 2021