lista = [1, 2, 3, 4, 5, 6]
aux = lista
print ("aux:", aux)
aux.pop(0)
aux.pop(1)
print ("aux post cambios:", aux)
print ("lista post cambios:", lista)
# Al modificar 'aux', también se modifica 'lista' 
# porque ambas variables apuntan a la 
# misma lista en memoria.
# eaea
