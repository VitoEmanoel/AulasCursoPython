"""
Repetições 
while (enquanto)
Executa uma ação enquanto a condição for verdadeira.
loop infinito -> Quando um código não tem fim, ou seja, a condição é sempre verdadeira.


"""
contador = 0

while contador <=100 :
    contador +=1  # contador = contador + 1

    if contador ==6 :
        print("Pulei o número 6")
        continue

    if contador >= 10 and contador <=27 :
        print("Pulei os número",contador)
        continue


    print(contador)

    if contador == 50 :
        break 

print("acabou")