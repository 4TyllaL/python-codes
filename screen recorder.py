import cv2
import numpy as np
import pyautogui
import PySimpleGUI as sg


SCREEN_SIZE = (1920, 1080)
fourcc = cv2.VideoWriter_fourcc(*"MJPG")
saida = cv2.VideoWriter("gravacao.mp4", fourcc, 20.0, (SCREEN_SIZE))

while True:
    img = pyautogui.screenshot()
    frame =  np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    saida.write(frame)
    print("Começou a gravar")

    if cv2.waitKey(1) == ord("q"):
        print("Gravação Encerrada")
        break

cv2.destroyAllWindows()
saida.release()