#Metodos para manipular cadenas
"""
def get_string_metodos():
    i=0
    for metodo in dir(str):
        if '__' not in metodo:
            i += 1
            print(i, metodo, sep=':')
get_string_metodos() """

# 1. capitalize cambia  mayuscula
"""
text = 'matias'

print(text.capitalize())"""
# 2. casefold cambia a minuscula
"""text = 'Matias'
print(text.casefold())"""

# 3. center
"""text = 'Matias'
print(text.center(20,'*'))
*******Matias*******"""

# 4. count
"""text = 'Matias'
print(text.count('a'))"""

# 5. endswith
"""text = 'Matias'
print(text.endswith('ds'))"""

# 6. expandtabs
"""text = 'abc\tabc'
print(text.expandtabs(10))"""

# 7. find y rfind
"""texto = 'Matias Gonzalez abc'
posición = texto.rfind('as')
print(posición)
print(texto[posición:])"""

# 8. format
"""text = '{asunto} al canal {accion} {nombre}'
print(text.format(asunto='suscribete', accion='ahora', nombre='Matias'))"""

# 9. format_map

"""coordenadas = {'x':60, 'y':20}
text = 'coordenadas:{x}, {y}'
print(text.format_map(coordenadas))"""

# 10. index
"""text = 'Matias'

print(text.index('t'))

# 11. isdecimal
text='123'
print(text.isdecimal())

# 12. isdigit

print(text.isdigit())
# 13. isnumeric

print(text.isnumeric())"""

# 13. islower y isupper
"""222text = 'GROVER'
print(text.isupper())
print(text.islower())"""

# 15. istitle
"""text = 'La Película Transformers'
print(text.istitle())"""

#16. lower, upper
"""text = 'GrovEr'
print(text.lower())
print(text.upper())"""

#17. join
"""text = '-'
print(text.join(['texto1', 'texto2', 'texto3']))"""

# 18. ljust, rjust
"""text = 'Grover'
print(text.ljust(20, '_'))"""

# 19. lstrip, rstrip
"""text = 'Suscríbete ahora'
print(text.lstrip('Sus'))"""

# 20. translate, maketrans
"""text = 'Prueba ahora'
table = text.maketrans('a', '5')
print(table)
print(text.translate(table))"""

# 21. partition
""""text = 'a+b=c=d'
print(text.rpartition('='))"""

# 22. removesuffix, removepreffix
"""text = 'WhatApp'
print(text.removeprefix('What'))
print(text.removesuffix('App'))"""

# 23. replace
"""text = 'Recuerda dejar tu comentario'
print(text)
print(text.replace('comentario', 'suscripcion'))
"""

# 24. split, lsplit, rsplit
text = 'Esto es una prueba de split'
print(text.rsplit(sep=' ', maxsplit=3))


