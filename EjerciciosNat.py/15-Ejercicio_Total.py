# Se ingresa el texto y se pasa todo a minuscula en la variable texto
texto = input("ingrese el texto: ").lower()

# Se crea una lista para agregar las letras a buscar
lista = []
lista.append(input("ingrese primera letra a consultar: "))
lista.append(input("ingrese segunda letra a consultar: "))
lista.append(input("ingrese tercera letra a consultar: "))

# Se consulta cuantas veces esta repetida cada una de las letras ingresadas
repeticion_a = texto.count(lista[0])
repeticion_b = texto.count(lista[1])
repeticion_c = texto.count(lista[2])

# Para mostrar en el texto ingreso los valores de la lista en variables asi
var_a = lista[0]
var_b = lista[1]
var_c = lista[2]
# Se imprime en pantalla el mensaje
print(f"""
      Repeticion de letras ingresadas
      1. letra "{var_a}" se repite {repeticion_a} veces
      2. letra "{var_b}" se repite {repeticion_b} veces
      3. letra "{var_c}" se repite {repeticion_c} veces""")

# Se agrega en lista el texto ingresado, separados por espacio
cadena_total_texto = texto.split()
# Se consulta el total de elementos y se guarda en una variable
total_cadena = len(cadena_total_texto)

# Se presenta al usuario cantidad de palabras
print(f"""
      Se encontraron un total de {total_cadena} palabras""")

# Se guarda la primera letra ubicada en [0]
# Se toma el tamaño del texto y luego se agrega la cantidad de caracteres -1
# Se asigna a una variable la ultima letra
primera_letra = texto[0]
ultima_letra = texto[-1]
cantidad_texto = len(texto)-1
ultima_letra = texto[cantidad_texto]

# Se muestra en pantalla la primera y ultima letra del texto
print(f"""
      La primera letra del texto es "{primera_letra}" 
      La ultima letra del texto es "{ultima_letra}" """)
# Se asigna a una variable el texto pero inverso
texto_inverso = texto[::-1]
# Se imprime en pantalla el texto inverso
print(f"""
      El Texto Original invertido es 
      "{texto_inverso}" """)

# Se consulta si la palabra Python se encuentra en el texto
# el resultado se guarda como Rta (true, false)
consultar = "python" in texto
# Se consulta en un dicionario la clave true o false
ConsultaTex = {True:"La Palabra Python si ",False:'La Palabra Python, no '}
Rta = ConsultaTex[consultar]
#Se imprime en pantalla
print(f"""
      Luego de Consultar su texto se pudo definir que {Rta}se encuentra en el texto
      """)





