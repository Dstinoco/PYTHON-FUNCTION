def carga_tributaria(preco, custo, lucro):
    imposto = preco - custo - lucro
    tributo = imposto / preco
    return tributo




preco = 2000
custo = 600
lucro = 1000


print('{:.1%}'.format(carga_tributaria(preco, custo, lucro)))

