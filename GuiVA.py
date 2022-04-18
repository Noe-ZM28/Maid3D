from tkinter import *
from PIL import ImageTk, Image
import pyautogui
import time


width, height= pyautogui.size()
pos_x = int(width/3)
pos_y = int(height/8)
width_screen = 600
height_screen = 400

main_window = Tk()
main_window.geometry(f"{width_screen}x{height_screen}+{pos_x}+{pos_y}")
#main_window.resizable(0, 0)
main_window.configure(background = 'black')

path_image = 'C:/Users/brink/Downloads/#Z/workspace/Maid3D/nezuko.jpg'
path_image2 = 'C:/Users/brink/Downloads/#Z/workspace/Maid3D/animes.jpg'

frame = Frame(main_window)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)
# Create an object of tkinter ImageTk
img = ImageTk.PhotoImage(Image.open(path_image))

# # Create a Label Widget to display the text or Image
label = Label(frame, image = img)
label.pack()






# def change_image_frame(image):
#     # Create a Label Widget to display the text or Image
#     img = ImageTk.PhotoImage(Image.open(image))
#     label = Label(frame, image = img)
#     label.pack()

# change_image_frame(path_image2)
main_window.mainloop()

