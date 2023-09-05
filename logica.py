es_amigo = True
es_familiar = False
"""if es_amigo and es_familiar:
  print('Es amigo y familiar')
elif es_amigo:
    print('Es amigo')
elif es_familiar:
    print('Es familiar')
else:
    print('No es amigo ni familiar')"""
    
#Operador Ternario
#condicion verdadera if condicion else condición falsa
mensaje = "Es amigo y familiar" if (es_amigo and es_familiar) else "No es amigo"
#print(mensaje)

#is vs ==
a = [1,2,3]
b = [1,2,3]
print(True == 1)
print('' == 1)
print([] == 1)
print(10 == 10.0)
print([] == [])
print(a == b)
print('')
print(True is 1)
print('' is 1)
print([] is 1)
print(10 is 10.0)
print([] is [])
print(a is b)