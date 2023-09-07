meta = 10000
vendas = {
    'joao': 15000,
    'julia': 27000,
    'marcus': 9900,
    'maria': 3750,
    'ana': 10300,
    'alon':7870,
}

def calculo_meta(meta, vendas):
    bateram_meta = []
    for vendedor in vendas:
        if vendas[vendedor] >= meta:
            bateram_meta.append(vendedor)
    perc_bateram_meta = len(bateram_meta) / len(vendas)
    return perc_bateram_meta, bateram_meta


p_meta, v_meta = calculo_meta(meta, vendas)

print('Total de {:.0%} bateram a meta'.format(p_meta))
print('Parabens aos Vendedores {}'.format(v_meta))


