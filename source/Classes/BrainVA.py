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

import sys

class Funtions:
    """
        Contiene los metodos correspondientes para la función del VA


        talk: Permite al asistente decir texto indicado

        listen: Permite a la computadora escuchar lo que dice el usuario

        write: escrebe lo que indica el usuario por medio de dictado,
        al terminar abre un archivo de texto con la información

        send_message_wha: Envia un mensaje al contacto indiado por la
        aplicación Web de Whatsapp

        send_message: [Desarrollo pendiente...]

        search: [Desarrollo pendiente...]

        faltan muchas aun :¨v
    """
    def __init__(self):
        """
        """
        #<----------------------------------------------------------------------------------------->
        self.name = "computadora"

        self.listener = sr.Recognizer()
        self.engine = pyttsx3.init()

        voices = self.engine.getProperty('voices')

        self.engine.setProperty('voice', voices[1].id) # 1 para español o 0 para ingles
        self.engine.setProperty('rate', 178)
        self.engine.setProperty('volume', 0.7)

        wikipedia.set_lang('es')

        self.diverEdgePath = Service("./Drivers/edgedriver_win64/msedgedriver.exe")
        self.user_profile = "C:/Users/brink/AppData/Local/Microsoft/Edge/User Data/Default"

        self.options = Options()
        self.options.binary_location = "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"
        user_profile = "C:/Users/brink/AppData/Local/Microsoft/Edge/User Data/Default"
        self.options.add_argument(f"--user-data-dir={user_profile}")
        self.options.add_argument(f"--profile-directory=Default")

        self.sites = {
            'google': 'https://www.google.com.mx/',
            'youtube': 'https://www.youtube.com/?gl=MX',
            'escuela': 'http://cursos2.tlalnepantla.tecnm.mx',
            'twitter': 'https://twitter.com/?lang=es',
            '': ''
        }
        self.files = {
            'notas': 'C:/Users/brink/Downloads/#Z/workspace/Maid3D/source/Files/notas.txt',
            '': ''
        }
        self.programs = {
            "navegador": "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe",
            "escritorio remoto": "C:/Program Files (x86)/TeamViewer/TeamViewer.exe",
            "lol": "C:/Riot Games/Riot Client/RiotClientServices.exe",
            "configuracion": "C:/Windows/System32/control.exe",
            "word": "C:/Program Files/Microsoft Office/root/Office16/WINWORD.EXE",
            "excel": "C:/Program Files/Microsoft Office/root/Office16/EXCEL.EXE",
            "power point": "C:/Program Files/Microsoft Office/root/Office16/POWERPNT.EXE",
            "": "",
        }
        self.contacts = {
            'yo': '+525620504753',
            'lala': '',
            'alina': '+525567038818'
        }

    def listen(self, SomeText = None):
        """
        """
        try:
            print(f'{SomeText}')
            with sr.Microphone() as source:
                voice = self.listener.listen(source)
                self.listener.adjust_for_ambient_noise(source, 0.5)
                rec = self.listener.recognize_google(voice,
                                                     language='es-MX')
                rec = rec.lower()
            
        except sr.UnknownValueError:
            #self.talk("Disculpa, no te he entendido, ¿me lo puedes repetir?")
            pass
        except UnboundLocalError:
            pass
        except Exception as e:
            exception_type, exception_object, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno

            print("Exception type: ", exception_type)
            print("File name: ", filename)
            print("Line number: ", line_number)

        return rec

    def talk (self, text):
        """
        """
        self.engine.say(text)
        self.engine.runAndWait()

    def talk_sites(self):
        if bool(self.sites) == True:
            self.talk("Has agregado las siguientes páginas web")
            for site in self.sites:
                self.talk(site)
        else:
            self.talk("¡Aún no has agregado páginas web!")

    def talk_programs(self):
        if bool(self.programs) == True:
            self.talk("Has agregado los siguientes programas")
            for program in self.programs:
                self.talk(program)
        else:
            self.talk("¡Aún no has agregado programas!")

    def talk_files(self):
        if bool(self.files) == True:
            self.talk("Has agregado los siguientes archivos")
            for file in self.files:
                self.talk(file)
        else:
            self.talk("¡Aún no has agregado archivos!")

    def talk_contacts(self):
        if bool(self.contacts) == True:
            self.talk("Has agregado los siguientes contactos")
            for cont in self.contacts:
                self.talk(cont)
        else:
            self.talk("¡Aún no has agregado contactos!")

    def play(self, music):
        pywhatkit.playonyt(music)
        print(f"Reproduciendo>: {music}")
        self.talk(f"Reproduciendo: {music}")

    def write(self, file):
        """
        """
        try: 
            self.talk('¿Que necesitas que escriba?:...')
            rec_write = self.listen("Escribiendo>: ")
            print(f"{rec_write}")  

            file.write(rec_write + os.linesep)
            file.close()
            subp.Popen("notas.txt", shell=True)
            self.talk('Terminé de escribir, este es el resultado')

        except Exception as e:
            exception_type, exception_object, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno

            print("Exception type: ", exception_type)
            print("File name: ", filename)
            print("Line number: ", line_number)

    def send_message_wha(self, contact, number):
        """
        """
        try: 
            self.talk("¿Que quieres que diga el mensaje?")
            message = self.listen("Escuchando mensaje>: ")
            print(message)
            pywhatkit.sendwhatmsg_instantly(number, message, 20, True, 5)
            print(f"Mensaje enviado a: {contact}")
            self.talk(f"Mensaje enviado a: {contact}")

        except Exception as e:
            exception_type, exception_object, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno

            print("Exception type: ", exception_type)
            print("File name: ", filename)
            print("Line number: ", line_number)

    def send_message(self, contact, number):
        """
        """
        try:
            pass
            self.talk("¿Que quieres que diga el mensaje?")
            message = self.listen("Escuchando mensaje>: ")
            print(message)

            driver = webdriver.Edge(service = self.diverEdgePath, options = self.options)

            driver.get(f"https://web.whatsapp.com/send?phone={number}&text={quote(message)}")

            driver.maximize_window()
            time.sleep(30)

            # Obtain button by link text and click.
            button = driver.find_element(by=By.CLASS_NAME, value = "_3HQNh _1Ae7k")
            button.click()

            self.talk(f"Mensaje enviado a {contact}")

        except Exception as e:
            exception_type, exception_object, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno

            print("Exception type: ", exception_type)
            print("File name: ", filename)
            print("Line number: ", line_number)

    def search(self, search):
        """
        """
        try:
            wiki = wikipedia.summary(search, 1)
            self.talk(f'Buscando...{search}')
            print(f"{search}>: {wiki}")
            self.talk(wiki)
            time.sleep(0.1)
            print(f'Busqueda terminada...')
            self.talk(f'Busqueda terminada...')
        except wikipedia.PageError:
            print(f"Disculpa, no encontré resultados para {search}.")
            self.talk(f"Disculpa, no encontré resultados para {search}.")
            pass
        except wikipedia.DisambiguationError:
            print(f"Lo siento, {search} es demasiado ambiguo, por favor sea mas claro en lo que quieres que busque.")
            self.talk(f"Lo siento, {search} es demasiado ambiguo, por favor sea mas claro en lo que quieres que busque.")
        except Exception as e:
            exception_type, exception_object, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno

            print("Exception type: ", exception_type)
            print("File name: ", filename)
            print("Line number: ", line_number)

    def open_something(self, something):
        """
        """
        try: 
            something = something.replace(' ', '')

            #<--------- P A G I N A S ---------------->
            if something in self.sites:
                for site in self.sites:
                    if site in something:
                        subp.call(f'start msedge.exe {self.sites[site]}', shell=True)
                        print(f"Abriendo página: {site}")
                        self.talk(f"Abriendo página: {site}")
                        break
            #<--------- P R O G R A M A S ------------>
            elif something in self.programs:
                for program in self.programs:
                    if program in something:
                        subp.Popen({self.programs[program]})
                        print(f"Abriendo programa: {program}")
                        self.talk(f"abriendo programa: {program}")
                        break
            #<--------- A R C H I V O S -------------->
            elif something in self.files:
                for file in self.files:
                    if file in something:
                        subp.Popen(f'{self.files[file]}', shell=True)
                        print(f"Abriendo archivo: {file}")
                        self.talk(f"abriendo archivo: {file}")
                        break
            else:
                print(f'Lo siento, [{something}] no se encuentra dentro de la información guardada')
                self.talk(f'Lo siento, {something} no se encuentra dentro de la información guardada')

        except Exception as e:
            print(f'{e}')

#Brain = Funtions()