from contextlib import ContextDecorator


def run():
    numero =  int(input('Escribe un número:'))
    contador=0
  

    for i in range (1, numero+1):
          
        if numero % i == 0 :
            contador+=1
          

            #print("residuo entero"+ str(contador))
               

        #else:
             
          # print( "residuo float")

    if contador == 2 :
        print("es primo")

    else:
         print("no es primoo")



if __name__ == '__main__' :
    run()

