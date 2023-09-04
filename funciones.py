#funciones basicas

def saludar(nombre):
    return (f'Hola {nombre}, desde la funcion')


saludo = saludar('matias')
print(saludo)

#def suma(a=0, b=0):
    #return (a + b)
def restar(a, b):
    return (a - b)
#sumar = suma(10,50)

#print('la suma es: ', sumar)

resta = restar (b=20, a=50)

#print('la resta es:', resta)

#funciones con argumentos indefinidos

def sumar(*args, **kwargs):
    suma = 0
    for n in args:
        suma += n
    
    return suma, kwargs
suma, datos = sumar(5,4,6, Ciudad = 'Viedma', edad = 42)

print('La suma es: ', suma)
print('datos:', datos)


