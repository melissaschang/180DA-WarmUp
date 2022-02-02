from pynput.mouse import Listener


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
        if text == 'knife':
            print("Move mouse up and down to chop")
            cooking=True
            print(cooking)
            return False


    else:
        print('stove')
        text=input('type spoon to stir')
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
        
while(True): 
    while (cooking==False):   
        with Listener(on_move=on_move, cooking=False) as listener:
            listener.join()
    while (cooking==True):
        print('yes')
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        plt.clear('all')
    


