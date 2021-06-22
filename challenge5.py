'''
Challenge 5- Play the waiting game

>>> waiting_game()

Your target time is 4 seconds
--- Press Enter to Begin ---

... Press Enter again after 4 seconds ...

Elapsed time: 4.213 seconds
(0.213 seconds too slow)
'''


import time,random
from pynput import keyboard

t = random.randrange(2,4,1)
print('Your target time is '+ str(t) + ' seconds')
print('... Press Enter again after '+str(t)+' seconds ...')
print('--- Press Enter to Begin ---')    
flag = True
start = 0
def f(key):
    global flag, start
    
    if flag:
        start = time.perf_counter()
    else:
        stop = time.perf_counter()
        diff = stop - start
        print('Elapsed time: '+ str(stop)+' seconds' )
        if diff == t:
            print('Bravo!! You made it (^_^)')
        elif diff > t:
            print('('+str(diff)+' seconds too slow)')
        elif diff < t:
            print('('+str(t-stop)+' seconds too fast)')
        return
    flag = False
            


with keyboard.Listener(on_press = f) as listener:
    listener.join()

