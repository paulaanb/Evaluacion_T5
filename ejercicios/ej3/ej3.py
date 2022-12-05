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
        return self.nombre  
        return self.propiedades
nombres =['Caballero','Guerrero','Arquero']  
propiedades = ['Vida','Ataque','Defensa','Alcance']
personas = []  
for x in nombres:     
    p = Persona(x)     
    personas.append(p.nombre)  
    print(personas)  
    fichero = open('personajes.pckl','wb') 
    pickle.dump(personas, fichero)  
    fichero.close() 

#Lectura de la clase personaje 
import pickle  
fichero = open('personajes.pckl','rb')  
personas = pickle.load(fichero) 
fichero.close()  
for x in personas:     
    print(x)


