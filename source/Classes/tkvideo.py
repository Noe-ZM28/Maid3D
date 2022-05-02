import threading
import imageio
from PIL import Image, ImageTk
from time import sleep
import sys

class tkvideo():
    """ 
        Main class of tkVideo. Handles loading and playing 
        the video inside the selected label.

        :keyword path: 
            Path of video file
        :keyword label: 
            Name of label that will house the player
        :param loop:
            If equal to 0, the video only plays once, 
            if not it plays in an infinite loop (default 0)
        :param size:
            Changes the video's dimensions (2-tuple, 
            default is 640x360) 
    
    """
    def __init__(self, label, path, loop = False, size = (640,360), Stop = False):
        self.path = path
        self.label = label
        self.loop = loop
        self.size = size
        self.Stop = Stop

    def load(self):
        """
            Loads the video's frames recursively onto the selected label widget's image parameter.
            Loop parameter controls whether the function will run in an infinite loop
            or once.
        """
        try:
            frame_data = imageio.get_reader(self.path)
            def play_video():
                for image in frame_data.iter_data():
                    frame_image = ImageTk.PhotoImage(Image.fromarray(image).resize(self.size))
                    self.label.config(image=frame_image)
                    self.label.image = frame_image
                    sleep(0.01)

                else:
                    pass
            if self.loop:
                while True:
                    play_video()
            else:
                play_video()
        except Exception as e:
            print(f"{e}")
    def play_Video(self):
        """
            Creates and starts a thread as a daemon that plays the video by rapidly going through
            the video's frames.
        """
        try: 
            self.thread = threading.Thread(target=self.load, name='Video')
            self.thread.daemon = 1
            self.thread.start()
            #algun dia encontraré la forma de cerrar este hilo xd
        except Exception as e:
            print(f"{e}")

