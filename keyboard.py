from pynput.keyboard import Key, Controller
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

def write_message(message):
    keyboard.type(message)

def type_message(message):
    for char in message:
        keyboard.press(char)
        keyboard.release(char)
        time.sleep(0.08)

def mineCobblestone():
    while(True):
        keyboard.press('w')
        time.sleep(1)
        keyboard.release('w')

        #mouse.move(200, 500)
        #mouse.click(Mouse.Button.left,1)
        position = mouse.position
        
        #mouse._position_set((position[0]+50, position[1]+100))
        mouse.press(Mouse.Button.left)
        time.sleep(1.5)
        mouse.release(Mouse.Button.left)
        time.sleep(0.2)


mouse = Mouse.Controller()
keyboard = Controller()
time.sleep(5)
#moveMinecraftPlayer()
mineCobblestone()
#type_message("Heyoooo Wen. What ya doing! \n Braaaaaaaaaaaaaah")