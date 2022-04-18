import pyttsx3
import pywhatkit
import speech_recognition as sr
import wikipedia
import subprocess as subp
import os
import json
import pywhatkit
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
import time
import webbrowser as web
from urllib.parse import quote



name = "computadora" 
listener = sr.Recognizer()
engine = pyttsx3.init()
KEY = None
diverEdgePath = Service("./Drivers/edgedriver_win64/msedgedriver.exe")
user_profile = "C:/Users/brink/AppData/Local/Microsoft/Edge/User Data/Default"

options = Options()
options.binary_location = "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"
options.add_argument(f"--user-data-dir={user_profile}")
options.add_argument(f"--profile-directory=Default")
voices = engine.getProperty('voices')


sites = {
    'google': 'https://www.google.com.mx/',
    'youtube': 'https://www.youtube.com/?gl=MX',
    'escuela': 'http://cursos2.tlalnepantla.tecnm.mx',
    'twitter': 'https://twitter.com/?lang=es',
    '': ''
}
files = {
    'notas': 'notas.txt',
    '': ''
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
contacts = {
    'yo': '+525620504753',
    'lala': '',
    '': ''
}

engine.setProperty('voice', voices[1].id) # 1 para español o 0 para ingles
engine.setProperty('rate', 178)
engine.setProperty('volume', 0.7)

def talk (text):
   engine.say(text)
   engine.runAndWait()

def listen(SomeText = None):
    try:
        print(f'{SomeText}')
        with sr.Microphone() as source:
            voice = listener.listen(source)
            listener.adjust_for_ambient_noise(source, 0.5)
            rec = listener.recognize_google(voice,
                                            key=KEY,
                                            language='es-MX')
            rec = rec.lower()
        
    except sr.UnknownValueError:
        talk("Disculpa, no te he entendido, ¿me lo puedes repetir?")

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

def send_message(contact, number):
    try: 
        talk("¿Que quieres que diga el mensaje?")
        message = listen("Escuchando mensaje>: ")
        print(message)

    #     driver = webdriver.Edge(service = diverEdgePath, options = options)

    #     driver.get(f"https://web.whatsapp.com/send?phone={number}&text={quote(message)}")

    #     driver.maximize_window()
    #     time.sleep(30)

    #     # Obtain button by link text and click.
    #     button = driver.find_element(by=By.CLASS_NAME, value = "_3HQNh _1Ae7k")
    #     button.click()

    #     talk(f"Mensaje enviado a {contact}")

    # except Exception as e:
    #     print(f"{e}")
        pywhatkit.sendwhatmsg_instantly(number, message, 20, True, 5)
        talk(f"Mensaje enviado a {contact}")

    except Exception as e:
        print(f"Error: {e}")


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
                    talk(f"Reproduciendo: {music}")

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
                    except FileNotFoundError:
                        file = open("notas.txt", "w")
                        write(file)

                elif 'envía' in rec:
                    contact = rec.replace('envia', '')
                    if 'mensaje' in rec: #arreglar
                        contact = rec.replace('mensaje', '')
                        for contact in contacts:
                            if contact in rec:
                                talk(f"enviando mensaje para: {contact}")
                                send_message(contact = contact, number = contacts[contact])
                    
                    if 'correo' in rec: #pendiente
                        contact = rec.replace('correo', '')

                elif "termina" in rec:
                    talk("Hasta pronto")
                    break
            elif "termina" in rec:
                talk("Hasta pronto")
                break
        except UnboundLocalError:
            continue
        except wikipedia.PageError:
            talk("Disculpa, no encontré resultados para la búsqueda indicada.")
            continue
        except Exception as e:
            print(f"Error: {e}")
            continue


if __name__ == '__main__':
    runVA()
