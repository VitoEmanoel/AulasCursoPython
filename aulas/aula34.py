"""
while (enquanto)
Executa uma acção enquento a condição for verdadeira.
loop infinito -> Qunado um código não tem fim, ou seja, a condição é sempre verdadeira.
"""
condicao= True

while condicao:
    nome = input('Digite seu nome: ')
    print(f'Olá {nome}!')

    if nome == 'sair':
        
        break
print('Saindo do loop...')