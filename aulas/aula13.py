nome = 'Victor'
altura = 1.70
peso = 57
imc =  peso / altura ** 2

#'F' significa formatação

linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'pesa{peso}Kg e seu imc é'
linha_3 = f'{imc:.2f}'

print (linha_1)
print (linha_2)
print (linha_3)
