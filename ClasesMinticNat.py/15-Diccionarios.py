#los diccionarios almacenan informacion en pares {clave:valor}

# diccionario = ¨{'c1':'valor1', 'c2':'valor2'}
# resultado = diccionario['c1']
# print(resultado)

cliente = {'nombre':'John', 'apellido':'Rojas', 'peso':88, 'talla':1.76}
#puedo consultar 
consulta = cliente['apellido']
print(consulta)
consulta = cliente['talla']
print(consulta)

dic = {'c1':55, 'c2':[10,20,30], 'c3':{'s1':100, 's2':200}}
#puedo acceder a un elemento conociendo su posicionamiento, con el valor 20 y el 200, como lo hariamos? :
print(dic['c2'][1])
print(dic['c3']['s2'])

dic2 = {'c1':['a','b','c'], 'c2':['d','e', 'f']}
#puedo generar un dato en mayuscula, en este caso lo haremos con la e
print(dic2['c2'][1].upper())

#asi puedo agregar una nueva clave o informacion en nuestro diccionario
dic3 = {1:'a', 2:'b'}
dic3[3]='c'
print(dic3)

#asi podemos modificar una clave
dic3[2]='D'
print(dic3)