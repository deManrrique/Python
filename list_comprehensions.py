# el un list compregension el ciclo es OBLIGATORIO.

"""def run():
    squares =[]
    for i in range(1,101):
        if i % 3 !=0
             squares.append(i**2)

    print(squares)

if __name__ == "__main__" :
    run()"""
from socket import if_indextoname


def run():
    squares=[i**2 for i in range(1,101)if i %3 !=0]
    print(squares)

if __name__ == "__main__" :


    run()

"""la list comprehensions se utilizan los [] y para los diccionarios se utilizan las {}"""

print("            ahora estas en dictionary comprehensions")
                         #DICTIONARY COMPREHENSONS

# en los dictionary comprehension la condición es OPCIONAL.
"""def run():
    my_dict={}
    for i in range(1,101):
        if i % 3 !=0:
             my_dict[i]=i**2

    print(my_dict)

if __name__ == "__main__" :
    run()"""

def run():
    my_dict = {i: i**2 for i in range(1,101)if i %3 !=0}
    print(my_dict)
if __name__ == "__main__" :
    run()


                        #RETO
#crear, con un dictionary comprehension, un diccionario cuyas llaves seas los 1.000 primeros números naturales con su raíces cuadradas como valores.

print("            MY RETO:  ")
"""
def run():
    my_dict = {i: i**0.5 for i in range(1,10000)}
    print(my_dict)
if __name__ == "__main__" :
    run()
"""
