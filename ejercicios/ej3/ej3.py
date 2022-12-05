#Creamos clase personaje
import pickle 
class Personaje:     
    def __init__(self,nombre):         
        self.nombre  = nombre          
    def __str__(self):        
        return self.nombre  
nombres =['Caballero','Guerrero','Arquero']  
personas = []  
for x in nombres:     
    p = Persona(x)     
    personas.append(p.nombre)  
    print(personas)  
    fichero = open('personajes.pckl','wb') 
    pickle.dump(personas, fichero)  
    fichero.close() 