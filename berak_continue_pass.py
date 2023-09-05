list = [1, 2, 3, 4, 5]

for item in list:
    #para pasar y usar luego
    pass



n = 1
while n <= len(list):
    print(n)
    n += 1
    if n == 3:
        continue
    print('No es 3')
    
    
"""while True:
    respuesta = input('ingrese un mensaje:')
    if(respuesta == 'bye'):
        print('Adios')
        break"""