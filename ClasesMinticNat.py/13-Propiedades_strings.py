#1. SON INMUTABLES: en este caso se genera error porque no puedo cambiar los datos del string
#nombre = "Karolina"
#entonces si quiero cambiar la K por una C
#nombre[0] = 'C'
#print(nombre)

#2. SON CONCATENABLES Y  3. MULTIPLICABLES se pueden unir con + o repetir con *
n1 = "Karo"
n2 = "lina"
print(n1+n2)
print(n1*5)

#4. SON MULTILINEABLES: se pueden escribir en varias lineas haciendo uso de las triples comillas asi:
poema = """
Del cielo cayo una rosa
mi madre la recogio
se la puso en la cabeza
y que linda que quedo
"""
print(poema)
#Estos tambien se pueden concatenar, ej:
print("""Esto es un poema 
que dice asi: """+(poema))

#5. PODEMOS VERIFICAR SU CONTENIDO, ES DECIR SI EXISTE O NO NUESTRA BUSQUEDA, SE USA in O not in
#el resultado es un booleano es decir true o false
print("agua" in poema)
print("agua" not in poema)

#6. PODEMOS DETERMINAR SU LONGITUD haciendo uso de la funcion len
print(len(poema))

