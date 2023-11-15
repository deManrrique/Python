""" numbers=[1,2,3,4]
numbers_v2=[]

for i in numbers:
    numbers_v2.append (i*2)
print(numbers)
print(numbers_v2) """
       #podemos hacer esto en una sola línea haciendo uso del MAP

from unittest import result


numbers=[1,2,3,4]
numbers_v2= list(map(lambda i: i*2, numbers))
print(numbers)
print(numbers_v2)
 
"""Hemos usado list() de forma que el objeto map se devuelve como una lista,
 en vez de como un objeto menos legible por el ser humano como <map object at 0x7fc250003a58>.
  El objeto map es un iterador sobre nuestros resultados, 
de forma que podríamos hacer un bucle con for o podemos usar list()
 para convertirlo en una lista. Estamos haciendo esto aquí porque es una buena forma de revisar los resultados."""

print("   ")
numbers_v3=[1,2,3,4,5]
numbers_v4=[1,1,1,1,1]

result=list(map(lambda x,y :x+y, numbers_v3,numbers_v4))
print(result)