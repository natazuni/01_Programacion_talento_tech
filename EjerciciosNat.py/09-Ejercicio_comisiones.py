
#Datos del usuario
Nombre_vendedor = input("Nombre: ")
Valor_ventas = float(input("Digite el valor de sus ventas: "))

#Comision
Total_comision = Valor_ventas*0.13
#print(round(Total_comision,2))


print(f"El total de comision que le corresponde a {Nombre_vendedor} por sus ventas es de {Total_comision}")
