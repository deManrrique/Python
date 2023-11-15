import random


def generar_password ():
    mayusculas= ['A','B', 'C', 'D', 'E', 'F', 'G']
    minusculas= ['a','b','c']
    simbolos=['!','@', '#']
    numeros= ['1','2','3','4','5']

    caracteres= mayusculas+ minusculas +simbolos+numeros

    password=[]

    #random en ingles es aleatorio

    for i in range(15):
        caracter_random = random.choice(caracteres)
        password.append(caracter_random)
       
        #para convertir una lista en un string hacemos lo siguiente>
    password = "".join(password)
        

    return password

def run():
    password = generar_password()
    print ("tu nueva contraseña es:  " + password)


if __name__ == '__main__' :
    run()
