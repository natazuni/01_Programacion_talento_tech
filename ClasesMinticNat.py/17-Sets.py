# SETS
# son conjuntos de datos
# son mutables, no son ordenados, no aceptan duplicados
# se puede crear con la palabra reservada set([]) o set({}) o set(())
mi_set= set([1,2,3,4])
print(type(mi_set))
mi_set=set({5,6,7,8,9})
print(type(mi_set))
mi_set=set((11,12,13,14))
print(type(mi_set))
mi_set2={1,2,3,4,5}
print(type(mi_set2))

# no permite duplicados
# mi_set{1,2,3,4,5,1,1,1,1} genera error
# se puede obtener la longitud del conjunto
print(len(mi_set))

# se pueden unir dos set con la opcion de set1.union(set2)
s1={1,2,3}
s2={3,4,5}
s3 = s1.union(s2)
print(s3)