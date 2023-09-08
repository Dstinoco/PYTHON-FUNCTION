def descobrir_servidor(email):
    try:
        posicao_a = email.index('@')
         
    except:
        raise Exception('email digitado é inválido!')
    
    else:
        servidor = email[posicao_a:]
        if 'gmail' in servidor:
            return 'gmail'
        elif 'yahoo' in servidor:
            return 'yahoo'
        elif 'hotmail' in servidor or 'outlook' in servidor or 'live' in servidor:
            return 'hotmail'
        elif 'uol' in servidor or 'bol' in servidor:
            return 'uol'
        else:
            return 'Não identificado'


email = input('Qual seu e-mail? ')    
print(descobrir_servidor(email))