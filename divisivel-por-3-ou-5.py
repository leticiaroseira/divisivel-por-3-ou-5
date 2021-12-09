numero_inteiro = int(input('Insira um número inteiro: '))
numero1 = numero_inteiro // 3
resto_1 = numero_inteiro % 3
numero2 = numero_inteiro // 5
resto_2 = numero_inteiro % 5
if resto_1 == 0:
    if resto_2 == 0:
        print('O número', numero_inteiro, 'é divisível por 3 e por 5')
    else:
        print(numero_inteiro)
else:
    print('O número', numero_inteiro, 'não é divisível por 3 e por 5')