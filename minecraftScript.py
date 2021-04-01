from pynput.keyboard import Key, Controller, Listener
import keyboard as kkeyboard
from pynput import mouse as Mouse
import pynput
import time

def moveMinecraftPlayer():
    while(True):
        keyboard.press('w')
        time.sleep(1)
        keyboard.release('w')

        keyboard.press('s')
        time.sleep(1)
        keyboard.release('s')

def strip_mine():
    i = 0
    while(True):
        #keyboard.press('w')
        #time.sleep(1)
        #keyboard.release('w')

        #mouse.click(Mouse.Button.left,1)
        mouse.move(0, -200)
        mouse.press(Mouse.Button.left)
        time.sleep(1.5)
        mouse.release(Mouse.Button.left)
        time.sleep(0.2)
        
        mouse.move(0, 200)
        mouse.press(Mouse.Button.left)
        time.sleep(1.5)
        mouse.release(Mouse.Button.left)
        time.sleep(0.2)

        #if i%20 == 0:
            #mouse.click(Mouse.Button.right,1)
        #i = i+1

def move_smooth(xm, ym, t):
    for i in range(t):
        if i < t/2:
            h = i
        else:
            h = t - i
        mouse.move(h*xm, h*ym)
        time.sleep(1/60)

def move_mouse():
    while(True):
        print(mouse.position)
        mouse.move(0,-100)
        #move_smooth(0,-1, 40)
        time.sleep(1)
        print(mouse.position)
        mouse.move(0, 100)
        time.sleep(1)
        

        #mouse.scroll(1,1)
        #mouse._position_set((position[0]+50, position[1]+100))

def move_mouse_with_keyboard():
    while(True):
        time.sleep(0.01)
        if kkeyboard.is_pressed('k'):
            mouse.move(0, -10)
        elif kkeyboard.is_pressed('j'):
            mouse.move(0, 10)
        elif kkeyboard.is_pressed('h'):
            mouse.move(-10, 0)
        elif kkeyboard.is_pressed('l'):
            mouse.move(10, 0)

mouse = Mouse.Controller()
keyboard = Controller()
listener = Listener()
time.sleep(5)
#move_mouse_with_keyboard()
#move_mouse()
strip_mine()
#moveMinecraftPlayer()
