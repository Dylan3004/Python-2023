import os
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def fun():
    text = " Abecadlo z pieca spadlo "
    while True:
        for i in range(5):
            clear_screen()
            print("\n" * i + text)
            time.sleep(0.5)
        for i in range(5):
            clear_screen()
            print("\n" * (5 - i) + text)
            time.sleep(0.5)

fun()



