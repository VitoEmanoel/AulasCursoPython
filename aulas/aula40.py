# calculadora com whilhe

while True:
    numero_1 = input('digite um numero: ')
    numero_2 = input('digite outro numero: ')
    operador = input('digite o operador(+-/*): ')

    numeros_validos = None

    try:
        num_1_float = float (numero_1)
        num_2_float = float (numero_2)
        numeros_validos = True

    except:
        numeros_validos = None
        
    if numeros_validos is None :
        print ('Um ou anbos os numeros digitados são inválidos')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador invalido')
        continue

    if len(operador) > 1:
        print ('Digite apenas um operador.')
        continue

    sair = input("quer sair ? [s]im: ").lower().startswith("s")

    if sair is True :
        break
    print(sair)
    
    
