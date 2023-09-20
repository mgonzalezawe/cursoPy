class PadreA:
    def __init__(self):
        print('Soy objeto PadreA')
    def a(self):
        print ('Soy metodo PadreA')

class PadreB:
    def __init__(self):
        print('Soy objeto PadreB')
    def b(self):
        print ('Soy metodo PadreB')
        
class HijoC(PadreA, PadreB):
    def c(self):
        print('Soy metodo de HijoC')

#Instancias
hijoc = HijoC()
hijoc.a()
hijoc.b()
hijoc.c()