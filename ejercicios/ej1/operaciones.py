def menu():
    print("Menu de operaciones.")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Salir")
    op = input ("Escriba la opcion:")
    op = int(op)
    if op==1: suma()
    elif op==2: resta()
    elif op==3: multiplicacion()
    elif op==4: division()
    else: exit()
    
def suma():
    try:
        print("")
        print ("Hacer sumas.")
        num1 = input("Numero 1: ")
        num2 = input("Numero 2: ")
        num1 = float(num1)
        num2 = float(num2)
    except TypeError:
       print('Error: No es posible dividir entre cero')
    print ("Resultado: ", num1+num2)
    print("")
    menu()
    
def resta():
    try:
        print("")
        print ("Hacer restas.")
        num1 = input("Numero 1: ")
        num2 = input("Numero 2: ")
        num1 = float(num1)
        num2 = float(num2)
    except TypeError:
       print('Error: No es posible dividir entre cero')
    print ("Resultado: ", num1-num2)
    print("")
    menu()
def multiplicacion():
    try:
        print("")
        print ("Hacer multiplicacion.")
        num1 = input("Numero 1: ")
        num2 = input("Numero 2: ")
        num1 = float(num1)
        num2 = float(num2)
    except TypeError:
       print('Error: No es posible dividir entre cero')
    print("")
    menu()
def division():
    try:
        print("")
        print ("Hacer division.")
        num1 = input("Numero 1: ")
        num2 = input("Numero 2: ")
        num1 = float(num1)
        num2 = float(num2)
    except ZeroDivisionError:
       print('Error: Tipo de dato no válido')
    except TypeError:
       print('Error: No es posible dividir entre cero')
    print ("Resultado: ", num1/num2)
    print("")
    menu()
menu()