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

from tkinter import Tk, Label, Button
from tkvideo import tkvideo
import pyautogui

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
            'notas': 'notas.txt',
            '': ''
        }
        self.programs = {
                "navegador": "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
                "escritorio remoto": "C:\Program Files (x86)\TeamViewer\TeamViewer.exe",
                "lol": "C:\Riot Games\Riot Client\RiotClientServices.exe",
                "configuracion": "C:\Windows\System32\control.exe",
                "word": "C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE",
                "excel": "C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE",
                "power point": "C:\Program Files\Microsoft Office\root\Office16\POWERPNT.EXE",
                "": "",
        }
        self.contacts = {
            'yo': '+525620504753',
            'lala': '',
            '': ''
        }

        #<------------------------------------------------->
        self.path_a = 'C://Users//brink//Downloads//#Z//workspace//Maid3D//source//Fellings//Test//a.mp4'
        self.path_b = 'C://Users//brink//Downloads//#Z//workspace//Maid3D//source//Fellings//Test//b.mp4'
        self.cut5 = 'C://Users//brink//Downloads//#Z//workspace//Maid3D//source//Fellings//Test//cut5.mp4'

        self.width, self.height= pyautogui.size()
        self.pos_x = int(self.width/3)
        self.pos_y = int(self.height/8)
        self.width_screen = 600
        self.height_screen = 400

        self.size_video = (self.width_screen-100,self.height_screen-100)

        self.main_window = Tk()
        self.main_window.geometry(f"{self.width_screen}x{self.height_screen}+{self.pos_x}+{self.pos_y}")
        self.main_window.resizable(0, 0)
        self.main_window.configure(background = 'black')

        self.my_label = Label(self.main_window)



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
            self.talk("Disculpa, no te he entendido, ¿me lo puedes repetir?")
        except UnboundLocalError:
            pass
        except Exception as e:
            print(f'{e}')

        return rec

    def talk (self, text):
        """
        """
        self.engine.say(text)
        self.engine.runAndWait()

    def write(self, file):
        """
        """
        try: 
            self.talk('¿Que necesitas que escriba?:...')
            rec_write = self.listen("Escribiendo>: ")
            print(f"{rec_write}")  

            file.write(rec_write + os.linesep)
            file.close()
            self.talk('Terminé de escribir, este es el resultado')
            subp.Popen("notas.txt", shell=True)

        except Exception as e:
            print(f'{e}')

    def send_message_wha(self, contact, number):
        """
        """
        try: 
            self.talk("¿Que quieres que diga el mensaje?")
            message = self.listen("Escuchando mensaje>: ")
            print(message)
            pywhatkit.sendwhatmsg_instantly(number, message, 20, True, 5)
            self.talk(f"Mensaje enviado a: {contact}")

        except Exception as e:
            print(f"Error: {e}")

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
            print(f"{e}")

    def search(self, search):
        """
        """
        try:
            wiki = wikipedia.summary(search, 1)
            self.talk(f'Buscando...{search}')
            print(f"{search}>: {wiki}")
            self.talk(wiki)
            time.sleep(0.1)
            self.talk(f'Busqueda terminada...')
        except wikipedia.PageError:
            self.talk(f"Disculpa, no encontré resultados para {search}.")
            pass
        except wikipedia.DisambiguationError:
            self.talk(f"Lo siento, {search} es demasiado ambiguo, por favor sea mas claro en lo que quieres que busque.")



    def start_Gui(self):
        """
        """
        button1 = Button(self.main_window, text="Video 1", command= lambda:self.replace_video(path_video = self.path_a))
        button1.pack()
        button2 = Button(self.main_window, text="Video 2", command= lambda:self.replace_video(path_video = self.path_b))
        button2.pack()

        player = tkvideo(label = self.my_label, path = self.cut5, loop = True, size = self.size_video)

        self.my_label.pack()
        player.play_Video()

        self.main_window.mainloop()

    def replace_video(self, path_video):
        """
        """
        try: 
            self.my_label.destroy()
            self.my_label = Label(self.main_window)
            player = tkvideo(label = self.my_label, path = path_video, loop = True, size = self.size_video, Stop=True)
            
            self.my_label.pack()
            player.play_Video()
            
        except Exception as e:
            print (f'Error: {e}')

