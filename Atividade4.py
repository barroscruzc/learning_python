from random import randint
# Primeiro criei uma lista que receberá os dicionários
# contendo as informações dos alunos à medida em que
# forem cadastradas.
lista_inscricoes = []


# Criei uma função simples, que irá destacar o título
# do menu, melhorando a visibilidade das informações
# exibidas.
def destaque(texto):
    print('-' * 15, texto, '-' * 15)


# Programa principal

# A função 'while True' é um laço de repetição
# infinita, que somente será interrompido quando
# o usuário selecionar a opção 'sair', que, por sua vez,
# conterá a instrução 'break' para interromper o loop e
# enfim finalizar o programa.
while True:
    destaque('MENU')
    print('Digite o número da opção desejada:')
    print('1 - Nova inscrição \n2 - Visualizar inscrição\n3 - Sair')
    num_menu = int(input(' '))

    # Ao selecionar a opção 1, serão solicitados os dados
    # para inscrição dos interessados no curso ofertado.
    if num_menu == 1:
        destaque('NOVA INSCRIÇÃO')
        nome = input('Digite nome: ')
        email = input('Digite E-mail: ')
        telefone = input('Digite telefone: ')
        curso = input('Digite Curso: ')
        # Usei a função 'randint' para gerar números aleatórios
        # entre 100 e 400.
        voucher = randint(100, 400)
        # Criando um dicionário contendo as palavras-chave
        # correspondentes ao tipo de informação e os seus
        # respectivos dados.
        aluno = {'voucher': voucher, 'nome': nome, 'email': email,
                 'telefone': telefone, 'curso': curso}
        # Com o 'append', o dicionário acima é inserido na lista
        # de inscrições.
        lista_inscricoes.append(aluno)

    # Ao escolher a opção 2 do menu, é exibida a lista geral
    # de inscritos, exibindo individualmente os dados cadastrados.
    # Para isso, utilizei as estruturas de repetição aninhadas
    elif num_menu == 2:
        print('LISTA DE INSCRITOS')
        # Com o contador abaixo, será exibido o número referente
        # à posição que cada inscrito ocupa na lista.
        codigo_aluno = 1
        for aluno in lista_inscricoes:
            destaque(('INSCRITO Nº {}'.format(codigo_aluno)))
            for tipo_info, info in aluno.items():
                print(' {} : {}' .format(tipo_info, info))
            codigo_aluno += 1

    # Ao selecionar a opção 3 do menu, interrompe-se o loop
    # e o programa prossegue para a próxima instrução, que
    # é o fechamento do programa.
    elif num_menu == 3:
        break

    # Caso o usuário digite valor diverso aos indicados
    # no menu, o programa informa o equívoco, e o loop
    # é reiniciado, exibindo o menu mais uma vez.
    else:
        print('Oops! Opção inválida, tente novamente...')
print('Encerrando programa...')
