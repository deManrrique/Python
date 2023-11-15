#                                               high order functions o funcion de orden superior

#es una función que recibice como parámetro a otra función

def saludo (func):
    func()

def hola():
    print("hola!!")

def adios():
    print("adios!!")

saludo(hola)
saludo(adios )

#hay 3 funciones de orden superior que son muy importantes en una gran cantidad de lenguajes de programación  son clásicos:

#                   FILTER, MAP Y  REDUCE
  
""" my_list=[1,2,5,6,7,8,,13,26,21]
odd= [i for in my_list if i % 2 !=0        <--------- esto mismo que esta en un list comprehensions lo puedo hacer un FILTER
print(odd) """


#uso con filter
my_list = [1,2,5,6,7,8,13,26,21]

odd = list(filter(lambda x: x%2 != 0, my_list))

print(odd)

#                      MAP
#tengo una lista de los números del 1 al 5 y lo que quiero hacer es convertira esta lista en la misma pero con los números elevados al cuadrado
#con list comprehensions:
"""      my_list= [1,2,3,4,5]
         squares [1**2 for i in my_list
         print(squares)     
 """
# uso con MAP
my_list = [1,2,3,4,5]

squares = list(map(lambda x: x**2 , my_list))

print(squares)



#                    REDUCE
"""      my_list = [2,2,2,2,2]
         all_multiplied = 1

         for i in my_list:
            all_multiplied = all_multiplied *1
        print(all_multiplied)                         
"""


#con reduce

#debo importar la función reduce del módulo functools porque no viene dentro del código de python directamente si en un módulo que está dentro de python que es functools

from functools import reduce
my_list = [2,2,2,2,2]

all_multiplied = reduce(lambda a, b: a*b, my_list)

print(all_multiplied)