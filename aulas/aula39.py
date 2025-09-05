"""
Interando strings com while

"""

#       0 1 2 3 4 5 6 7 8 9 10 11 12 13
#       V I C T O R   E M A N O  E  L
#      14 12 11 10 9 8 7 6 5 4 3 2 1 
nome = "Victor Emanoel" # Interáveis

# tamanho_nome = len(nome)
# print(tamanho_nome)
# print(nome[tamanho_nome -14]) # Acessando a ultima letra
# print(nome[-14]) # Acessando a ultima letra
indice = 0
novo_nome = ''

while indice < len(nome):
    letra = nome[indice]
    novo_nome +=f'*{letra}'
    indice +=1
novo_nome += '*'

print(novo_nome)
    