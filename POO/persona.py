class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def getdatos(self):
        print(f'Nombre: {self.nombre} \t {self.edad}')
        

#Herencia
class Usuario(Persona):
    def getdatos(self):
        return 'Datos del usuario', super().getdatos()
        #print(f'Datos del usuario: {self.nombre}, Edad {self.edad}')

class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.sueldo = sueldo

    def getdatos(self):
        #return super().getdatos()
        print(f'Datos del Empleado, Nombre: {super().getdatos()}, {self.sueldo}')

