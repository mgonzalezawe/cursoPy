productos = ['notebooks', 'lentes', 'iPhones', 'parlantes', 'iphones']

productos[0] = 'laptops'
new_products = productos.copy()
new_products [0]="PC"
new_products.append('printer')

new_products.extend(productos)
new_products.insert(1,"teclado")
#productos.clear()
#productos.pop(2)
#if "parlantes" in productos:
    #productos.remove("parlantes")
#print(productos.index("lentes"))
#print(productos)
#print(productos.count("lentes"))
#productos.reverse()
#print(productos)
productos.sort()
print(productos)