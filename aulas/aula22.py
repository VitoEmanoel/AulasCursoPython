# Operadores lógicos 
# and (e) or (ou) not (não)
# and - todas as condições precisam ser verdadeiras 
# Se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele valor 
# são considerados falsy (que você já viu)
# 0 0.0 '' False
# Também existe o tipo None que é 
# usado para representar um não valor 


# entrada = input( '[E]ntrar [S]air: ')

# senha_digitada = input ('Digite sua Senha: ')

# senha_permitida = '1234'

# if entrada == ('E' or  entrada == 'e') and  senha_digitada == senha_permitida:
#     print('Entar')
# else :
#     print('Sair')

# avaliação de curto circuito 
senha = input ('Digite sua Senha: ') or 'Você não digitou sua senha'
print (senha)