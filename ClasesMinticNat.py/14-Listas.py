mi_lista =['a','b','c','d']

#si quiero saber que clase de sprint es este hago lo siguiente:
print(type(mi_lista))

#podemos conocer su longitud con el uso de len
resultado = len(mi_lista)
print(resultado)

#podemos hacer indexacion de c, es decir si yo quiero saber cual es el posicionamiento de la 'c' 
resultado = mi_lista.index('c')
print(resultado)

#para obtener un fragmento de la lista usando los []
resultado = mi_lista[0:2]
print(resultado)

#podemos concatenar las listas es decir unir +
mi_lista2 = ['d','e','f','g']
resultado = mi_lista + mi_lista2
print(resultado)

#puedo cambiar un elemento por otro, en este caso cambiar 'a' por la palabra 'alfa'
mi_lista[0] = 'alfa' #para esto utilizamos el posiscionamiento del elemento que quiero cambiar
print(mi_lista)

#puedo agregar un elemento a la lista usando la funcion append
mi_lista.append('z')
print(mi_lista)

#puedo eliminar un elementop de la lista usando la funcion pop y el posiscionamiento del elemento a eliminar
mi_lista.pop() #si no coloco nada eliminara elelemento final
print(mi_lista)

mi_lista.pop(1)
print(mi_lista)

# puedo ordenar los elementos de la lista con la funcion sort
mi_lista.sort()
print(mi_lista)

# puedo invertir el orden de los elementos de la lista con la funcion reverse
mi_lista.reverse()
print(mi_lista)
