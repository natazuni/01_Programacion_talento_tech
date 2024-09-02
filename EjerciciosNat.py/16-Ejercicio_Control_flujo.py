# Ejercicio Control de flujo Practica 1
num1= int(input("ingresa un numero: "))
num2 = int(input("Ingresa otro numero: "))
if num1 > num2:
     print(f"{num1} es mayor que {num2}")
elif num2 > num1:
     print(f"{num2} es mayor que {num1}")
else:
     print(f"{num1} y {num2} son iguales")
    

#  Ejercicio Control de flujo Practica 2
licencia = 'si'in input("Tiene Licencia responda si o no: ").lower()
edad = int(input("Ingrese su edad: "))

if licencia and edad >= 18:
     print("puedes conducir")
elif edad < 18 and licencia == False:
     print("no puedes conducir, para ello debes tener 18 años y contar con una licencia")
elif edad >= 18 and licencia == False:
     print("no puedes conducir. Necesitas contar con una licencia")
else:
     print("Verifica los datos porque no puedes tener licencia si tienes menos de 18 años")

# Ejercicio Control de flujo Practica 3
Habla_ingles = 'si' in input("Hablas ingles (responde si o no): ").lower()
Sabe_Python =  'si' in input("Programas en Python (responde si o no): ").lower()

if Habla_ingles and Sabe_Python:
    print("Cumples con los requisitos para postulare")
elif Habla_ingles == False and Sabe_Python:
    print("Para Postularte, necesitas tener conocimiento en Ingles")
elif Sabe_Python== False and Habla_ingles:
    print("Para Postularte, necesitas saber programar en Python")
else:
    print("Para Postularte, necesitas saber programar en Python y tener conocimiento en Ingles")