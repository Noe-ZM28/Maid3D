from Classes.BrainVA import Funtions
from Classes.tkvideo import tkvideo
from tkinter import Tk, Label, Button
import pyautogui
import threading
import sys

class GUIVA():
    def __init__(self):
        self.Brain = Funtions()
        self.path_a = 'C://Users//brink//Downloads//#Z//workspace//Maid3D//source//Fellings//Test//a.mp4'
        self.path_b = 'C://Users//brink//Downloads//#Z//workspace//Maid3D//source//Fellings//Test//b.mp4'
        self.path_c = 'C://Users//brink//Downloads//#Z//workspace//Maid3D//source//Fellings//Test//c.mp4'

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

        button1 = Button(self.main_window, text="On", command= self.hilo_runVA)
        button1["bg"] = "white"
        button1.pack()

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
            print(f"{e}")

    def runVA(self):
        while True:
            try:
                rec = self.Brain.listen("Esperando instrucción")   
                print(f"Escuchando>: {rec}")  
                if self.Brain.name in rec:
                    rec = rec.replace(self.Brain.name, '')

                    if 'reproduce' in rec:
                        music = rec.replace('reproduce','')
                        self.Brain.play(music)

                    elif 'repite' in rec:
                        repeat = rec.replace('repite','')
                        self.Brain.talk(repeat)

                    elif 'busca' in rec:
                        search = rec.replace('busca', '')
                        self.Brain.search(search)

                    elif 'abre' in rec:
                        something = rec.replace('abre', '')
                        self.Brain.open_something(something)

                    elif 'escribe' in rec:
                        writte = rec.replace('escribe', '')
                        try:
                            with open("C:/Users/brink/Downloads/#Z/workspace/Maid3D/source/Files/notas.txt", "a") as file:
                                self.Brain.write(file)
                        except FileNotFoundError:
                            file = open("C:/Users/brink/Downloads/#Z/workspace/Maid3D/source/Files/notas.txt", "w")
                            self.Brain.write(file)

                    elif 'envía' in rec:
                        contact = rec.replace('envia', '')
                        if 'mensaje' in rec: #arreglar
                            contact = rec.replace('mensaje', '')
                            for contact in self.Brain.contacts:
                                if contact in rec:
                                    self.Brain.talk(f"enviando mensaje para: {contact}")
                                    self.Brain.send_message_wha(contact = contact, number = self.Brain.contacts[contact])
                        
                        if 'correo' in rec: #pendiente
                            contact = rec.replace('correo', '')
                            self.Brain.talk(f"Función no disponible")
                            self.Brain.send_email(contact)
                            

                    elif "termina" in rec:
                        self.Brain.talk("Hasta pronto")
                        break
                elif 'video 1' in rec:
                    video = rec.replace('video 1','')
                    self.Brain.talk(f'reproduciendo: {rec}')
                    self.replace_video(self.path_b)
                elif 'video 2' in rec:
                    video = rec.replace('video 2','')
                    self.Brain.talk(f'reproduciendo: {rec}')
                    self.replace_video(self.path_a)
                elif 'video 3' in rec:
                    video = rec.replace('video 3','')
                    self.Brain.talk(f'reproduciendo: {rec}')
                    self.replace_video(self.path_c)
                elif "termina" in rec:
                    self.Brain.talk("Hasta pronto")
                    break
            except UnboundLocalError:
                continue
            except Exception as e:
                print(f"{e}")

    def hilo_runVA(self):
        try: 
            thread = threading.Thread(target=self.runVA, name='Asistente V')
            thread.daemon = 1
            thread.start()
            return thread #algun dia encontraré la forma de cerrar este hilo xd
        except Exception as e:
            print(f"{e}")

    def start(self):
        self.main_window.mainloop()

# player = tkvideo(label = self.my_label, path = path_c, loop = True, size = size_video)
# self.my_label.pack()
# player.play_Video()
#<----------------------------------------------------------------------------------->


GUIVA().start()
