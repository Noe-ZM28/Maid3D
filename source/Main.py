from Classes.BrainVA import Funtions
from Classes.tkvideo import tkvideo
from tkinter import Tk, Label, Button
import pyautogui
import threading
import sys


Brain = Funtions()
#<----------------------------------------------------------------------------------->
path_a = 'C://Users//brink//Downloads//#Z//workspace//Maid3D//source//Fellings//Test//a.mp4'
path_b = 'C://Users//brink//Downloads//#Z//workspace//Maid3D//source//Fellings//Test//b.mp4'
cut5 = 'C://Users//brink//Downloads//#Z//workspace//Maid3D//source//Fellings//Test//cut5.mp4'
cut = 'C://Users//brink//Downloads//#Z//workspace//Maid3D//cut.mp4'

width, height= pyautogui.size()
pos_x = int(width/3)
pos_y = int(height/8)
width_screen = 600
height_screen = 400

size_video = (width_screen-100,height_screen-100)

main_window = Tk()
main_window.geometry(f"{width_screen}x{height_screen}+{pos_x}+{pos_y}")
main_window.resizable(0, 0)
main_window.configure(background = 'black')

my_label = Label(main_window)
#<----------------------------------------------------------------------------------->

#<----------------------------------------------------------------------------------->
def replace_video(path_video):
    """
    """
    try:
        global my_label
        my_label.destroy()
        my_label = Label(main_window)
        player = tkvideo(label = my_label, path = path_video, loop = True, size = size_video, Stop=True)
        
        my_label.pack()
        player.play_Video()
        
    except Exception as e:
        exception_type, exception_object, exception_traceback = sys.exc_info()
        filename = exception_traceback.tb_frame.f_code.co_filename
        line_number = exception_traceback.tb_lineno

        print("Exception type: ", exception_type)
        print("File name: ", filename)
        print("Line number: ", line_number)

def runVA():
    while True:
        try:
            rec = Brain.listen("Esperando instrucción")   
            print(f"Escuchando>: {rec}")  
            if Brain.name in rec:
                rec = rec.replace(Brain.name, '')

                if 'reproduce' in rec:
                    music = rec.replace('reproduce','')
                    Brain.play(music)

                elif 'repite' in rec:
                    repeat = rec.replace('repite','')
                    Brain.talk(repeat)

                elif 'busca' in rec:
                    search = rec.replace('busca', '')
                    Brain.search(search)

                elif 'abre' in rec:
                    something = rec.replace('abre', '')
                    Brain.open_something(something)

                elif 'escribe' in rec:
                    writte = rec.replace('escribe', '')
                    try:
                        with open("notas.txt", "a") as file:
                            Brain.write(file)
                    except FileNotFoundError:
                        file = open("notas.txt", "w")
                        Brain.write(file)

                elif 'envía' in rec:
                    contact = rec.replace('envia', '')
                    if 'mensaje' in rec: #arreglar
                        contact = rec.replace('mensaje', '')
                        for contact in Brain.contacts:
                            if contact in rec:
                                Brain.talk(f"enviando mensaje para: {contact}")
                                Brain.send_message_wha(contact = contact, number = Brain.contacts[contact])
                    
                    if 'correo' in rec: #pendiente
                        contact = rec.replace('correo', '')
                        Brain.talk(f"Función no disponible")

                elif "termina" in rec:
                    Brain.talk("Hasta pronto")
                    break
            elif 'video 1' in rec:
                video = rec.replace('video 1','')
                Brain.talk(f'reproduciendo: {rec}')
                replace_video(path_a)
            elif 'video 2' in rec:
                video = rec.replace('video 2','')
                Brain.talk(f'reproduciendo: {rec}')
                replace_video(path_b)
            elif 'video 3' in rec:
                video = rec.replace('video 3','')
                Brain.talk(f'reproduciendo: {rec}')
                replace_video(path_b)
            elif "termina" in rec:
                Brain.talk("Hasta pronto")
                break
        except UnboundLocalError:
            continue
        except Exception as e:
            exception_type, exception_object, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno

            print("Exception type: ", exception_type)
            print("File name: ", filename)
            print("Line number: ", line_number)

def hilo_runVA():
    thread = threading.Thread(target=runVA, name='Asistente V')
    thread.daemon = 1
    thread.start()
    return thread #algun dia encontraré la forma de cerrar este hilo xd

#<----------------------------------------------------------------------------------->

#<------------------------------------- G U I---------------------------------------------->
try:
    button1 = Button(main_window, text="On", command= hilo_runVA)
    button1["bg"] = "white"
    button1.pack()

    player = tkvideo(label = my_label, path = cut5, loop = True, size = size_video)
    my_label.pack()
    player.play_Video()
    #<----------------------------------------------------------------------------------->

    main_window.mainloop()

except Exception as e:
    exception_type, exception_object, exception_traceback = sys.exc_info()
    filename = exception_traceback.tb_frame.f_code.co_filename
    line_number = exception_traceback.tb_lineno

    print("Exception type: ", exception_type)
    print("What happend?: ", exception_object)
    print("File name: ", filename)
    print("Line number: ", line_number)
