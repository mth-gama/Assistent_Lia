import os
import datetime as dt
import wikipedia as wik
import speech_recognition as sr
import pyautogui as pg
import random
import pyttsx3 as ptt
from Funcoes_LIA import *
import pyaudio

maquina = ptt.init('sapi5')
nome = 'Matheus'
maquina.say('Comando de voz ativado')
maquina.runAndWait()
audio = sr.Recognizer()

with sr.Microphone() as source:
    maquina.say('O microfone está OK')
    maquina.runAndWait()
    print('Ouvindo...')
    voz = audio.listen(source)
    # comando = audio.recognize_google(voz, 'pt-BR')
    # comando = comando.lower()
    # saber_horas(maquina, nome)
    # if 'executa um arquivo' in comando:
    #     executar_arquivo(maquina, nome)
    # elif 'que horas' in comando:
    #     saber_horas(maquina, nome)
    # elif 'conta uma piada' in comando:
    #     contar_piada(maquina)
    # elif 'sair' in comando:
    #     maquina.say('Saindo do sistema, até mais '+nome)
    #     maquina.runAndWait()
