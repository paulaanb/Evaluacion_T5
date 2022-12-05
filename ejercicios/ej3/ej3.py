from io import open
#Creamos clase personaje
import pickle 
class Personaje:     
    def __init__(self,nombre, vida, ataque, defensa, alcance):         
        self.nombre  = nombre  
        self.vida = vida 
        self.ataque = ataque
        self.defensa = defensa
        self.alcance = alcance   
    def __str__(self):
        return "{} = {}vida, {} ataque, {}defensa, {}alcance".format(self.nombre, self.vida, self.ataque, self.defensa,self.alcance)    
#Creamos clase gestor
class Gestor:
    personajes = []

    def __init__(self):
        self.cargar
    def agregar(self,p):
        for pTemp in self.personajes:
            if pTemp.nombre = p.nombre
            return
        self.personajes.append(p)
        self.guardar()
    def borrar(self, nombre):
        for pTemp in self.personajes:
            if pTemp.nombre == nombre:
                self.personajes.remove(pTemp)
                self.guardar()
                print("\nEl personaje {} ha sido borrado".format(nombre))
                return
    def mostrar(self):
        if len(self.personajes) == 0:
            print("El gestor esta vacio.")
            return
        for p in self.personajes:
            print(p)
    def cargar(self):
        fichero = open('personajes.pckl', 'ab+')
        fichero.seek(0)
        try:
            self.personajes = pickle.load(fichero)
        except:
            pass 
        finally:
            fichero.close()
            print("El personaje {} se ha cargado en el fichero".format(len(self.personajes)))
            