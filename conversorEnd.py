

def conversor(tipo_pesos, valor_dolar):
    pesos = input("¿Cuántos pesos " + tipo_pesos + " tienes? :")
    pesos = float(pesos)
    dolares =  pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print ("Tienes $" + dolares + "dólares")

menu = """
Bienvenidos al  conversor de  monedas
1- Pesos Colombianos
2- Pesos Argentinos
3- Pesos Mexicanos

Elige una opción
"""



opcion = int(input(menu)) #por qué  aparece si no está imprimiendo?

if opcion == 1:
    conversor("Colombianos", 3875)
elif opcion == 2:
    conversor("Argentinos", 65)
elif opcion ==3:
    conversor("mexicanos" , 24)
else:
    print("Ingresa una opción  correcta por Favor ;)")