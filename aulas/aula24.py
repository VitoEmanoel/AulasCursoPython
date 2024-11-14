# operadores in e not in 
# strings são interáveis
#  0 1 2 3 4 5
#  V i c t o r 
# -6-5-4-3-2-1

# nome = 'Victor'
# print(nome[2])
# print(nome[-4])
# print('vio' in nome)
# print('zero' in nome)
# print(10 * '-')
# print('vio' not in nome)
# print('zero' not in nome)
nome = input ( 'Digite seu nome: ')
encontrar = input('Digite oque deseja encontrar: ')
if encontrar in nome : 
    print(f'{encontrar} está em {nome}')
else :
    print(f'{encontrar} Mão está em {nome}')