from moviepy.editor import *
  

video = 'C:/Users/brink/OneDrive/Documentos/Camtasia/Proyecto taller de investigacion/Proyecto taller de investigacion.mp4'

clip = VideoFileClip(video) 
  
clip = clip.subclip(267, 319)

  
clip.write_videofile('funcionamiento_2.mp4')