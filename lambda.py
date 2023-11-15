#una funcion es simplemente código que escribimos una vez y que vamos a aplicar después en diferentes lugares de lo que estemos trabajando. 
#         ¿Te acuerdas cómo se crea una función?

#colocamos def luego un identificador que es el nombre de nuestra fución los parametros de la misma que van entre paréntesis dejamos dos puntos":" y debajo en un nuevo bloque de código el contenido de la función


#                      FUNCIONES ANÓNIMAS  O lambdas
# son funciones que no tienen un identificador (osea no tienen nombre)
# pueden tenerlos argumentos que queramos, pero solo en una línea de código
# no necesitamos poner la palabra return en una función anónima ya que de por retorna siempre

# sintaxis:            Lambda argumentos: expresión
#          palindrome= lambda string: string == string[::-1]
#print(palindrome("ana"))

#con el nombre de la variable Palindrome vamos a llamar a la función. ya que la función está dentro de la variable

#el ejemplo con funciones normales:
"""def palindrome(string):
     return string==string[::-1]
    print (palindrome('ANA'))"""

# ejemplo con Lambda:

palindrome= lambda string: string == string[::-1]
print(palindrome("ana"))





