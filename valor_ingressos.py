total_idades = 0
total_clientes = 0
total_vendas = 0
while True:
    print('Para sair, digite 0')
    idade = int(input('Qual sua idade?'))
    if idade >= 12:
        ingresso = 30
        total_idades += idade
        total_clientes += 1
        total_vendas += ingresso
        print('O ingresso custa R$ {}' .format(ingresso))
    elif idade < 12 and idade > 3:
        ingresso = 15
        total_idades += idade
        total_clientes += 1
        total_vendas += ingresso
        print('O ingresso custa R$ {}' .format(ingresso))
    elif idade <= 3 and idade > 1:
        ingresso = 0
        total_clientes += 1
        total_idades += idade
        total_vendas += ingresso
        print('O ingresso custa R$ {}' .format(ingresso))
    else:
        break
print('Foram vendidos {} ingressos.' .format(total_clientes))
print('Total em caixa: R${}'.format(total_vendas))
print('A média de idades dos clientes é {} anos'.format(total_idades / total_clientes))
