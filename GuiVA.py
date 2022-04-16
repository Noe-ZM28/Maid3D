import pyttsx3
import pywhatkit
import speech_recognition as sr

import wikipedia

import subprocess as subp
import os
import json

from tkinter import *
from pygame import mixer
from PIL import Image, ImageTk

main_window = Tk()
main_window.title("Asistente")
main_window.geometry("400x400")
main_window.resizable(0, 0)
main_window.configure(background="#BEABF9")


name = "computadora" 
listener = sr.Recognizer()
engine = pyttsx3.init()
KEY = None

voices = engine.getProperty('voices')


sites = {
    'google': 'google.com',
    'youtube': 'youtube.com',
    'escuela': 'http://cursos2.tlalnepantla.tecnm.mx',
    'twitter': 'https://twitter.com/?lang=es'
}
files = {
    'notas': 'notas.txt'
}
programs = {
        "navegador": "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        "escritorio remoto": "C:\Program Files (x86)\TeamViewer\TeamViewer.exe",
        "lol": "C:\Riot Games\Riot Client\RiotClientServices.exe",
        "configuracion": "C:\Windows\System32\control.exe",
        "word": "C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE",
        "excel": "C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE",
        "power point": "C:\Program Files\Microsoft Office\root\Office16\POWERPNT.EXE",
        "": "",
}

engine.setProperty('voice', voices[1].id) # 1 para español o 0 para ingles
engine.setProperty('rate', 178)
engine.setProperty('volume', 0.7)

def talk (text):
   engine.say(text)
   engine.runAndWait()

def listen(Something = None):
    try:
        print(f'{Something}')
        with sr.Microphone() as source:
            voice = listener.listen(source)
            listener.adjust_for_ambient_noise(source, 0.5)
            rec = listener.recognize_google(voice,
                                            key=KEY,
                                            language='es-MX')
            rec = rec.lower()
        
    except sr.UnknownValueError:
        pass
        #talk("Disculpa, no te he entendido, ¿me lo puedes repetir?")
    except wikipedia.PageError:
        talk("Disculpa, no te he entendido, ¿me lo puedes repetir?")
        pass
    except:
        pass
    return rec

def write(file):
    talk('¿Que necesitas que escriba?')
    rec_write = listen("Escribiendo>: ")
    print(f"{rec_write}")  

    file.write(rec_write + os.linesep)
    file.close()
    talk('Terminé de escribir, este es el resultado')
    subp.Popen("notas.txt", shell=True)

def runVA():
    while True:
        try:
            rec = listen("Esperando instrucción")   
            print(f"Escuchando>: {rec}")  
            if name in rec:
                rec = rec.replace(name, '')


                if 'reproduce' in rec:
                    music = rec.replace('reproduce','')
                    pywhatkit.playonyt(music)
                    print(f"Reproduciendo>: {music}")
                    talk(f"Reproduciendo {music}")


                elif 'repite' in rec:
                    repeat = rec.replace('repite','')
                    talk(repeat)


                elif 'busca' in rec:
                    search = rec.replace('busca', '')
                    wikipedia.set_lang('es')
                    wiki = wikipedia.summary(search, 1)
                    talk(f'Buscando...{search}')
                    print(f"{search}>: {wiki}")
                    talk(wiki)


                elif 'abre' in rec:
                    any = rec.replace('abre', '')
                    for any in sites:
                        if any in rec:
                            talk(f"abriendo {any}")
                            subp.call(f'start msedge.exe {sites[any]}', shell=True)
                    for any in programs:
                        if any in rec:
                            talk(f"abriendo {any}")
                            subp.Popen({programs[any]})


                elif 'archivo' in rec:
                    file = rec.replace('abre', '')
                    for file in files:
                        if file in rec:
                            talk(f"abriendo {file}")
                            subp.Popen(f'{files[file]}', shell=True)


                elif 'escribe' in rec:
                    writte = rec.replace('escribe', '')
                    try:
                        with open("notas.txt", "a") as file:
                            write(file)
                    except FileNotFoundError as e:
                        file = open("notas.txt", "w")
                        write(file)


                elif "termina" in rec:
                    talk("Hasta pronto")
                    break
            elif "termina" in rec:
                talk("Hasta pronto")
                break


        except UnboundLocalError:
            continue
        except:
            continue


main_window.mainloop()
runVA()