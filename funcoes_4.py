def padronizar_codigos(lista_codigo, padrao='m'):
    for i, item in enumerate(lista_codigo):
        item = item.replace('  ', ' ')
        item = item.strip()
        if padrao == 'm':
            item = item.casefold()

        elif padrao == 'M':
            item = item.upper()

        lista_codigo[i] = item
    return lista_codigo        
    


codigos = ['abc123 ', ' ASD321', 'wsd852', 'LGH123', 'ewq123', 'opl573']


print(padronizar_codigos(codigos, padrao='m'))
