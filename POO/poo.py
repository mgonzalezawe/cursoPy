class Persona:
    def __init__(self, nom, ed, tel):
        self.nombre = nom
        self.edad = ed
        self.telefono = tel
    
    def getDatos(self):
        print('Nombre: ', self.nombre)
        print('Edad: ', self.edad)
        print('Telefono: ', self.telefono)
    

