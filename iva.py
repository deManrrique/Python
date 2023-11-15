amount =  int(input("introduce el valor del producto: "))

"""en ingles amount es Monto.
   invoice es factura
   vat es Iva"""
def iva(amount, vat=0.19):
    only_vat = amount * vat
    price_with_vat= only_vat +amount
    return  print("el iva es: "+ str(int(only_vat)) +"\n" +
    " monto total: "+ str(int(price_with_vat)))
   
iva(amount)