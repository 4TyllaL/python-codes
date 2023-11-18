from tkinter.constants import CENTER
from tkinter import Button, messagebox
from PySimpleGUI.PySimpleGUI import Checkbox, Element, WINDOW_CLOSED, Window
from pytube import YouTube
import PySimpleGUI as sg
import os 

#Criar a o programa
class Tela:
    def __init__(self):
        layout = [
            [sg.Text("Digite a URL :"), sg.Input(key="linkT")],
            [sg.Checkbox("Vídeo", key="video"), sg.Checkbox("Áudio", key="audio"), sg.Checkbox('Playlist', key="playlist")],
            [sg.Button("BAIXAR")]
        ]
        self.window = sg.Window("DownTube", layout)

    def iniciar(self):
        while True:
            event, self.values = self.window.read()

            if event == sg.WINDOW_CLOSED:
                break

            if event == "BAIXAR":
                self.baixar()

    def baixar(self):
        url = self.values["linkT"]
        download_folder = os.path.expanduser("~")
        download_folder = os.path.join(download_folder, "Downloads")

        if self.values['video']:
            link = url
            video = YouTube(link)
            stream = video.streams.get_highest_resolution()

            base_filename = stream.title + ".mp4"
            full_path = os.path.join(download_folder, base_filename)
            count = 1

            while os.path.exists(f"{full_path}.mp4"):
                base_filename = f"{stream.title} ({count})" + ".mp4"
                full_path = os.path.join(download_folder, base_filename)
                count += 1

            try:
                stream.download(output_path=download_folder, filename=base_filename)
                sg.popup("Aviso !", "VÍDEO BAIXADO COM SUCESSO !")
            except Exception as e:
                sg.popup_error("Erro", f"Ocorreu um erro ao baixar o vídeo: {str(e)}")

        if self.values["audio"]:
            link = url
            audio = YouTube(link)
            stream = audio.streams.get_audio_only()

            base_filename = audio.title + ".mp4"
            full_path = os.path.join(download_folder, base_filename)
            count = 1

            while os.path.exists(f"{full_path}.mp4"):
                base_filename = f"{audio.title} ({count})" + ".mp4"
                full_path = os.path.join(download_folder, base_filename)
                count += 1

            try:
                stream.download(output_path=download_folder, filename=base_filename)
                sg.popup("Aviso!", "Áudio Baixado Com Sucesso!")
            except Exception as e:
                sg.popup_error("Erro", f"Ocorreu um erro ao baixar o áudio: {str(e)}")

tela = Tela()
tela.iniciar()
