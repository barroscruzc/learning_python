conjunto = []
n = int(input('Quantos números deseja inserir no conjunto?'))
for i in range(0, n, 1):
    novo_num = float(input('Digite o {} número: \n'.format(i + 1)))
    while novo_num < 0 or novo_num > 1000:
        print('Ops! Digite um número entre 0 e 1000')
        novo_num = float(input('Digite o {} número: \n'.format(i + 1)))
    conjunto.append(novo_num)

conjunto.sort()
print("O menor valor digitado é: {}".format(conjunto[0]))
print("O maior número digitado é: {}".format(conjunto[n - 1]))
print("A soma de todos os valores é: {}".format(sum(conjunto[:])))