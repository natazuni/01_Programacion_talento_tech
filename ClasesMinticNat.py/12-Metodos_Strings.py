mi_texto = "Este es un texto implementado en Python"

#Metodo Upper
#Metodo para cambiar todos mis caracteres en mayusculas
resultado = mi_texto.upper()
print(resultado)

#Metodo Lower
#Metodo para cambiar todos mis caracteres en minusculas
resultado = mi_texto.lower()
print(resultado)

#Tambien puedo cambiar un caracter o un cadena de caracteres a minuscula o mayuscula
resultado = mi_texto[3].upper()
print(resultado)

resultado = mi_texto[11:16].lower()
print(resultado)

#Metodo split
#Metodo para generar una separacion (espacios en blanco)
resultado = mi_texto.split()
print(resultado)

resultado = mi_texto.split("t")
print(resultado)

#Metodo join
#Metodo para unir
palabra1 = "Aprender"
palabra2 = "Python"
palabra3 = "es"
palabra4 = "facil"

frase = " ".join([palabra1,palabra2,palabra3,palabra4])
print(frase)

