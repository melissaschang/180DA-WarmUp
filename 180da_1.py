import time
from pynput import keyboard
from pynput.mouse import Listener
from threading import Thread


last_positionx = None
text = None
cooking = False

def on_move(x, y):
    #cooking=False
    global last_positionx
    if last_positionx:
        if x > last_positionx+10:
            print('moving right')
        elif x < last_positionx-10:
            print('moving left')
    last_positionx = x
    #print(x)
    if x>=1920/2:
        print('chopping board')
        text= input("Type knife to chop: ")
        main.status='pause'
        if text == 'knife':
            print("Move mouse up and down to chop")
            cooking=True
            print(cooking)
            return False


    else:
        print('stove')
        text=input('type spoon to stir')
        main.status='pause'
        if text=='spoon':
            print("move mouse in circle to stir")
            cooking=True
            print(cooking)
            return False




'''
listener.start()
try:
    listener.wait()
    with_statements()
finally:
    listener.stop()
'''
def on_move_call(): 
    while(True): 
        while (cooking==False):   
            with Listener(on_move=on_move) as listener:
                listener.join()
        while (cooking==True):
            print('yes')
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
            plt.clear('all')


def main():
    main.status = 'run'

    while True:
        print('running')
        time.sleep(1)

        while main.status == 'pause':
            time.sleep(1)

        if main.status == 'exit':
            print('Main program closing')
            break


Thread(target=main).start()
Thread(target=on_move_call).start()
