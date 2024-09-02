# si es se usa if(si) - el elif quiere decir que hay otra condicion - si no es se usa else(si no)
if 10 > 9:
    print("Es correcto")

if True:
    print("Es correcto")

x = True
if x:
    print("Es correcto")
    
if 5 == 2:
    print("si es igual")
else:
    print("No es igual")  
    
mascota = 'gato'
if mascota == 'perro':
    print("Tienes un perro")
elif mascota == 'gato':
    print("Tienes un gato")
elif mascota == 'tucan':
    print("Tienes un tucan")
else:
    print("No es una mascota")  

edad = 15
calificacion = 5
if edad < 18:
    print("Eres menor de edad")
else:
    print("Eres adulto")      

a = 5
if a == 4:
    print("es tres")
elif a < 4:
    print ("segunda verificacion")
else:
    print("negacion")
    
# for
letras = ('a','b','c','d','e')    
for item in letras:
    print(item)

# while
numeros = (2,4,6,8,10)
contador = 0
while contador < 4:
    print(f"numero {numeros[contador]}")
    contador+= 1

# range
for i in range(1,11):
    print(i)
    