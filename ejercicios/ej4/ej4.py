import plataform
import os
import time
import datatime

def limpiar_pantalla():
    time.sleep(2)

        if platform.system() == 'Windows':
            os.system('cls')
        else:
            os.system('clear')
if __name__ == '__main__':
    limpiar_pantalla()

fecha_actual = datatime.datatime.now()

fecha_actual
print(type(fecha_actual))
print(fecha_actual.strftime('%d/%m/%Y %H:%M:%S'))