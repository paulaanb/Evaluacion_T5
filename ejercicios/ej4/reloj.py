import platform
import os
import time
import datetime

def limpiar_pantalla():
    time.sleep(2)

    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
if _name_ == '_main_':
    limpiar_pantalla()

fecha_actual = datetime.datetime.now()

fecha_actual
print(type(fecha_actual))
print(fecha_actual.strftime('%d/%m/%Y %H:%M:%S'))