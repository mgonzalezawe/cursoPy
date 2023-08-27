"""num = int (input('ingrese un numero: '))

if num != 0:
    if num > 0:
        if num % 2 == 0:
            print(f'El {num} es Par +')
        else:
            print(f'El {num} es Impar +')
    elif num % 2 == 0:
            print(f'El {num} es Par -')
    else:
            print(f'El {num} es Impar -')        
else:
    print(f'El {num} es neutro')       
  """

"""vocal = input('ingrese un dato:')
if vocal == 'a':
    print(vocal, 'es vocal')
elif vocal == 'e':
    print(vocal, 'es vocal')
elif vocal == 'i':
    print(vocal, 'es vocal')
elif vocal == 'o':
    print(vocal, 'es vocal')
elif vocal == 'u':
    print(vocal, 'es vocal')
else:
    print(vocal, 'no es vocal')
    """
    
#while
"""num = int (input('ingrese un numero: '))
cont = 1
suma = 0
while cont <= num:
    suma += cont
    cont += 1
print(suma)"""


#MOSTRAR EL NUMERO MENOR DE N NUMEROS INGRESADOS
"""n = int(input('cantidad de numeros:'))
menor = 0
i = 1
while(i <= n):
    numero = int(input('numero: '))
    if i == 1:
        menor = numero
    elif numero < menor:
        menor = numero
    i += 1
print (f'El numero menor es: {menor}')"""

"""palabras = ['Gato', 'León', 'Avión', 'Auto']
for p in palabras:
    print(p, len(p))"""
    
"""for i in range(5):
    print(i+10)"""

Lista = list(range(0,20,3))
print(Lista)
