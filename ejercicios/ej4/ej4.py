import plataform
import os
import time

def limpiar_pantalla():
    time.sleep(2)

        if platform.system() == 'Windows':
            os.system('cls')
        else:
            os.system('clear')
if __name__ == '__main__':
    limpiar_pantalla()