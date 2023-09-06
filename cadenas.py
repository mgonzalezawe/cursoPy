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

# 8. 

