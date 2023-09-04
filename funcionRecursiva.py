def factorial(numero):
    if numero > 1:
        numero = numero * factorial(numero - 1)
    return numero

#numero = int(input('Ingrese un numero: '))

#print('El factorial es: ', factorial(numero))

def contadorAtras(numero):
    numero -= 1
    if numero > 0:
        print(numero)
        contadorAtras(numero)
    else:
        print('FIN')
        
    print('Liberación:  {numero}')
contadorAtras(5)