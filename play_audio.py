# pip install playsound
from playsound import playsound

audio_file_beep = "mp3/cash_register.mp3"
audio_file_cam = "mp3/phone_camera.mp3"


# playsound(audio_file_cam)

file_name = audio_file_beep
s = open(file_name, 'rb').read()
print(s)