"""
tupla es una esctrutura propia de python que permine almacenrnar datos   y  no puede cambiar

"""

tupla=(1,2,3)
print(tupla)
tupla2=(7,"oscar",True,450.1,16+7j,15,"felicidad",False)
print(tupla2)
tupla3=(9,3,(4,5,6))
print(tupla3)
print(tupla2[1])
print(tupla2[0:4])
print(tupla2[-2])
a,b,c=tupla
print(a)
print(b)
print(c)

tuplafinal=tupla+tupla3
print(tuplafinal)

print(tuplafinal.count(3))

print(tuplafinal.index(3))
