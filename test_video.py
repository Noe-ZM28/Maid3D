from tkinter import Tk, Label, Button
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
my_label.pack()

player = tkvideo(label = my_label, path = path_a, loop = True, size = size_video)
player.play()

def replace_video(label, path_video):
    label.destroy()
    label = Label(main_window)
    label.pack()

    player = tkvideo(label = label, path = path_video, loop = True, size = size_video)
    player.play()
    
button = Button(main_window, text="Click Me", command= lambda:replace_video(my_label, path_b))
button.pack()

main_window.mainloop()
