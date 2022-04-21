from json import load
from tkinter import Tk, Label, Button

from requests import delete
from tkvideo import tkvideo
import pyautogui

path_a = 'C://Users//brink//Downloads//#Z//workspace//Maid3D//a.mp4'
path_b = 'C://Users//brink//Downloads//#Z//workspace//Maid3D//b.mp4'
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
player = tkvideo(label = my_label, path = path_b, loop = True, size = size_video)
my_label.pack()
player.play_Video()

def replace_video(player, path_video):
    player = tkvideo(label = my_label, path = path_video, loop = True, size = size_video)
    player.play_Video()
    
button = Button(main_window, text="Click Me", command= lambda:replace_video(player=player, path_video = path_a))
button.pack()

main_window.mainloop()
