#Definimos la clase

class Player:
    #Atriburto de obejto de clase
    menbresia = True
    
    def __init__(selft, nombre= 'anonimo', edad= 0):
        selft.nombre = nombre
        selft.edad = edad
        
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
    def agregar

