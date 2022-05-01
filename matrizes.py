#  logica de programacao e algoritmos
#  estrutura de dados - matrizes


cinema = []

for i in range(10):
    linha = []
    for j in range(10):
        linha.append('O')
    cinema.append(linha)

while True:
    print("""
1 - Reservar
2 - Layout do Cinema
3 - Sair""")

    opcao = input('')

    if opcao == '1':
        fila = int(input('Fila'))
        poltrona = int(input('Poltrona'))

        if cinema[fila][poltrona] == 'O':
            cinema[fila][poltrona] = 'X'
        else:
            print("A poltrona já está ocupada!")

    elif opcao == '2':
        print("""
|            TELA             |
|_____________________________|
""")
        for i in range(10):
            for j in range(10):
                lugar = cinema[i][j]
                print(f' {lugar} ', end='')
            print('')
    else:
        print('Encerrando...')
        break
