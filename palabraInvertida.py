"""Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida 
empezando 
por la última."""

print("""Hola te invertiremos tu palabra cuantas veces quieras
 si deseas salir de nuestro juego solo debes introducir la palabra "salir" """)

while True:
    

    inverted_word =  str(input("introduce una palabra "))
    new_inverted_word=inverted_word[::-1]
    

    if inverted_word == ("salir"):
        print("saliste el juego, vuelve pronto :D")
        break

    print("tu palabra invertida es:  " + new_inverted_word)