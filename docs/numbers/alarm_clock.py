# Alarm Clock - A simple clock where it plays a sound after X number of minutes/seconds or at a particular time.

from playsound import playsound
from datetime import datetime


playsound('xylophone-loop.mp3')

current_time = datetime.now().strftime("%H:%M:%S")


# def now() -> datetime.datetime:
#     return datetime.datetime.now()