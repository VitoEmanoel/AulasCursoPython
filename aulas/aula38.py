"""

Repetição 
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> quando um codigo não tem fim 

"""
qtd_coluna = 5
qtd_linhas = 5

linha = 1

while linha <= qtd_linhas:
    coluna = 1
    while coluna <= qtd_coluna :
        print (f"Linha:{linha}, Coluna:{coluna}")
        coluna +=1
    linha +=1

print("acabou")