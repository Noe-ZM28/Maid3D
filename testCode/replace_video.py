
import threading
import imageio
from PIL import Image, ImageTk
from time import sleep
from tkinter import Tk, Label, Button


class tkvideo():
    def __init__(self, label, path, size = (500,300)):
        self.path = path
        self.label = label
        self.size = size
    def load(self):
        try:
            frame_data = imageio.get_reader(self.path)
            while True:
                for image in frame_data.iter_data():
                    frame_image = ImageTk.PhotoImage(Image.fromarray(image).resize(self.size))
                    self.label.config(image=frame_image)
                    self.label.image = frame_image
                    sleep(0.01)

        except Exception as e:
            print(f"{e}")

    def play_Video(self):
        try: 
            self.thread = threading.Thread(target=self.load, name='Video')
            #self.thread.daemon = 1
            self.thread.start()
        except Exception as e:
            print(f"{e}")

image = "C:/Users/brink/Downloads/#Z/workspace/Maid3D/Master.gif"
main_window = Tk()
main_window.geometry(f"600x400")

my_label = Label(main_window)

a = tkvideo(label = my_label, path = image)
a.play_Video()
main_window.mainloop()