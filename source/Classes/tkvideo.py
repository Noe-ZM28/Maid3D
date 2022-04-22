import threading
import imageio
from PIL import Image, ImageTk
from time import sleep
from tkinter import Label

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

    def load(self, path, loop, label):
        """
            Loads the video's frames recursively onto the selected label widget's image parameter.
            Loop parameter controls whether the function will run in an infinite loop
            or once.
        """

        frame_data = imageio.get_reader(path)
        def play_video():
            for image in frame_data.iter_data():
                frame_image = ImageTk.PhotoImage(Image.fromarray(image).resize(self.size))
                label.config(image=frame_image)
                label.image = frame_image
                sleep(0.01)

            else:
                pass
        if loop:
            while True:
                play_video()
        else:
            play_video()

    def play_Video(self):
        """
            Creates and starts a thread as a daemon that plays the video by rapidly going through
            the video's frames.
        """
        try: 
            thread = threading.Thread(target=self.load, args=(self.path, self.loop, self.label))
            thread.daemon = 1
            thread.start()
            return thread #algun dia encontraré la forma de cerrar este hilo xd
        except Exception as e:
            exception_type, exception_object, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno

            print("Exception type: ", exception_type)
            print("File name: ", filename)
            print("Line number: ", line_number)
