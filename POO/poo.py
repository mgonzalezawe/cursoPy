class Persona:
    """nombre = None
    edad = None
    telefono = None"""
    def __init__(self, nom, ed, tel):
        self.nombre = nom
        self.edad = ed
        self.telefono = tel
    
    def getDatos(self):
        print('Nombre: ', self.nombre)
        print('Edad: ', self.edad)
        print('Telefono: ', self.telefono)
    
#instancia de la clase Persona  
per1 = Persona('matias', 43, 451531351)
per2 = Persona('pablo', 85, 5645436) 
per3 = Persona('Ana', 22, 151515)

per1.getDatos()
print('='*10)
per2.getDatos()
print('='*10)
per3.getDatos()