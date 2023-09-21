import math

class Figura:
    def __init__(self):
        pass
    
    def area(self):
        pass
    
    def perimetro():
        pass

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
        
    def area(self):
        return math.pi * self.radio ** 2 
    def perimetro(self):
        return 2 * math.pi * self.radio

class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado
        
    def area(self);
        return self.lado ** 2
    
    def perimetro(self):
        return 4 * self.lado
        