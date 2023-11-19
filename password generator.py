import random
import PySimpleGUI as sg
import os

from PySimpleGUI.PySimpleGUI import Input

class PassGen:
    def __init__(self):
        sg.theme("Black")
        layout = [
            [sg.Text("Site/Software", size=(10, 1)), sg.Input(key="site",size=(20, 1))],
            [sg.Text("Usuario",size=(10, 1)), sg.Input(key="user",size=(20, 1))],
            [sg.Text("Quantidade de caracteres"), sg.Combo(values=list(range(30)), key="total_chars", default_value=1, size=(3, 1))],
            [sg.Output(size=(32, 5))],
            [sg.Button("Gerar Senha")]
        ]
        self.janela = sg.Window("PyGen",layout)
    
    def iniciar(self):
        while True:
            evento, valores = self.janela.read()
            if evento == sg.WINDOW_CLOSED:
                break
            if evento == "Gerar Senha":
                new_passs = self.gerar_senha(valores)
                print(new_passs)
                self.save(new_passs, valores)


    def gerar_senha(self,valores):
        char_list = "ABCDEFGHIJKLMNOPQRSTUVXYZabcdefghijlmnopqrstuvxz1234567890!@#$%¨&*"
        char = random.choices(char_list, k=int(valores["total_chars"]))
        new_pass = ''.join(char)
        return new_pass


    def save(self, new_passs, valores):
        with open ("senhas.txt", "a", newline="") as arquivo:
            arquivo.write(f"site: {valores['site']}, usuario: {valores['user']}, nova senha:{new_passs} ")

        print("Arquivo salvo")
        

gen = PassGen()
gen.iniciar()