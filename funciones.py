#así declaro una función
"""
 def imprimir_mensaje():
    print('mensaje especial: ')
    print('Estoy aprendiendo a usar funciones')

imprimir_mensaje() #de este modo invoco  la funcion 3 veces
imprimir_mensaje()
imprimir_mensaje() """

def conversacion(mensaje):
     print ('Hola')
     print('cómo estás?')
     print(mensaje)
    
     print('Adios')


opcion= int(input("Elige una opción (1,2,3): "))
if opcion==1:
   conversacion("elegiste la opcion: 111" )
elif opcion==2:
    conversacion("elegiste la opcion: 2" )
elif opcion==3:
     conversacion("elegiste la opcion: 333" )
else:
    print ('escriba una opcion correcta')
