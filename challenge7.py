'''
Challenge 7: Set an alarm

>>> set_alarm(time.time()+1,'alarm.wav','Wake up!')
'''
import time
from playsound import playsound

def set_alarm(t, tone, msg):
    diff = t - time.time()
    time.sleep(diff)
    print(msg)
    playsound(tone)


path = 'E:/Waste of Time/Songs/S.mp3'
set_alarm(time.time()+1 , path, 'Wake up!')
