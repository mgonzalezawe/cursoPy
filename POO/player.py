#Definimos la clase

class Player:
    #Atriburto de obejto de clase
    menbresia = True
    
    def __init__(self, nombre= 'anonimo', edad= 0): #por default si pongo = algo
        self.nombre = nombre
        self.edad = edad
        
    def ejecutar(self):
        print('run')
        return 'Ok'
    
    def datos(self):
        print(f'mi nombre es {self.nombre}')
        
    def getMenbresia(self):
        if Player.menbresia:
            print('Ok')
        else:
            print('No')
    @classmethod
    def agregar_datos(cls, score):
        #return score
        return cls('Pedro', 25)
    
    @staticmethod
    def agregar_datos2(score):
        return score
        

