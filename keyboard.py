from pynput.keyboard import Key, Controller
from pynput import mouse as Mouse
import pynput
import time



def write_message(message):
    keyboard.type(message)

def type_message(message):
    for char in message:
        keyboard.press(char)
        keyboard.release(char)
        time.sleep(0.08)

def move_mouse():
    while(True):
        mouse.move(200,500)
        time.sleep(1)

        position = mouse.position
        
        #mouse._position_set((position[0]+50, position[1]+100))





mouse = Mouse.Controller()
keyboard = Controller()
time.sleep(5)
move_mouse()
#type_message("Heyoooo Wen. What ya doing! \n Braaaaaaaaaaaaaah")