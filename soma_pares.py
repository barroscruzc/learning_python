while True:
    x = int(input('Escreva um número inteiro: \n'))
    if x % 2 == 0 and x != 0:
        par = x
        soma = x
        for pares in range(4):
            par += 2
            soma += par
        print(f'A soma dos 5 números pares consecutivos a {x} é {soma}')
        continue
    elif x % 2 != 0:
        par = x + 1
        soma = par
        for i in range(4):
            par += 2
            soma += par
        print(f'A soma dos 5 números pares consecutivos a {x} é {soma}')
        continue
    else:
        quit()

