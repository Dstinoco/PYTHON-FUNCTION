def preco_final(preco, **kwargs):
    if 'desconto' in kwargs:
        preco *= (1 - kwargs['desconto'])
    if 'garantia_extra' in kwargs:
        preco += kwargs['garantia_extra']
    if 'imposto' in kwargs:
        preco *= (1 + kwargs['imposto'])
    return preco           


print(preco_final(2000, garantia_extra = 200, desconto=0.1, imposto=0.4))