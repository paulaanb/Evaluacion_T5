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


