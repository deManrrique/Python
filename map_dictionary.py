items = [
    {
        'product':'camisa',
        'price': 100
        
    },
    {
        'product':'pantalones',
        'price':300,
    }
]

prices = list(map(lambda item : item['price'],items))
print(prices)
#me imprime solo el precio de los diccionarios porque así le dije a la lambda que lo hiciera. 

def add_taxes(item):
    item['taxes']=item['price']*.19
    return item
new_items = list(map(add_taxes, items))
print(new_items)

#con esta función agrego otro elemento a mi diccionario que son los impuestos(taxes) 