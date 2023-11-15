from random import randint

def run():
    N= randint(0,20)
    numero =  int(input('Escribe un número del 0 al 20:'))
    while numero != N:
        
        if numero>N:
            print('más pequeño')
        elif numero<N:
            print('más grande')
        
     
        numero =  int(input('Escribe un número:'))
        


    #if N== numero:
    print('ganaste')


if __name__ == '__main__' :
    run()
