
#Diccionarios
personas = ['Grover', 40, 1.75]

persona = {
    'nombre': 'Grover',
    'edad': 40,
    'size': 1.75,
    'gadget': ['iPhone', 'iPad', 'Audifono'],
    'casado': True,
     15: 'ok'
     }
#print(persona['gadget'][1])

#persona['direccion'] = 'Lima'

#lista = persona['gadget']
print(persona.get('edad', 35))
#persona.clear()
#print(persona.keys())
#print(persona.values())
#print(persona.items())
#persona.pop('edad')
#persona.update({'mascota': False})
#print(persona)
#for k, v in persona.items():
#    print(k, v)
#print(len(persona))