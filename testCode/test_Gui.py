from tkinter import Tk, Label, Button
from Classes.tkvideo import tkvideo
import pyautogui

path_a = 'C://Users//brink//Downloads//#Z//workspace//Maid3D//source//Fellings//Test//a.mp4'
path_b = 'C://Users//brink//Downloads//#Z//workspace//Maid3D//source//Fellings//Test//b.mp4'
cut5 = 'C://Users//brink//Downloads//#Z//workspace//Maid3D//source//Fellings//Test//cut5.mp4'

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

def replace_video(path_video):
    try: 
        global my_label
        my_label.destroy()
        my_label = Label(main_window)
        player = tkvideo(label = my_label, path = path_video, loop = True, size = size_video, Stop=True)
        
        my_label.pack()
        player.play_Video()
        
    except Exception as e:
        print (f'Error: {e}')


button1 = Button(main_window, text="Video 1", command= lambda:replace_video(path_video = path_a))
button1.pack()
button2 = Button(main_window, text="Video 2", command= lambda:replace_video(path_video = path_b))
button2.pack()

my_label = Label(main_window)
player = tkvideo(label = my_label, path = cut5, loop = True, size = size_video)

my_label.pack()
player.play_Video()

main_window.mainloop()