#un igual (=) es asignacion 2 iguales (==) es comparacion y (!=) es diferente de 
mi_bool = 10 == 25
mi_bool = 'blanco' == 'blanco'
print(mi_bool)

4 < 5
5 < 6
mi_bool = 4 < 5 < 6
print(mi_bool)

#tambien lo podemos implementar de esta manera otra comparacion
mi_bool = (4 < 5) and (5 < 6)
#El and incluye todas las condiciones, cuando necesitamos que todas se generen para que todas las comparaciones puedan ser verdad
mi_bool = (55 == 55) and ('perro' == 'perro')
#Tambien podemos usar or, cuando necesitamos que todas se generen en este caso las comparaciones pueden ser verdad o falsas 
mi_bool = (10 == 10) or (3 == 3)

texto = "esta es una frase breve"
mi_bool = ("frase" in texto) and ('python' in texto)
print(mi_bool)

mi_bool=("esta" in texto) or ("python" in texto)
print(mi_bool)