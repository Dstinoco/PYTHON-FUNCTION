def minha_soma(*args):
    soma = 0
    for num in args:
        soma += num
    return soma    

resultado = minha_soma(10, 20, 30, 40)
print(resultado)