dicio_hospedes = {'G': 'GATO', 'C': 'CÃO', 'R': 'RATO', 'O': 'OSSO', 'Q': 'QUEIJO'}


# Função para melhorar a visibilidade do jogo, destacando
# o título da fase ou menu em que se encontra.
def destaque(texto):
    print('-' * 25, texto, '-' * 25)


# Com a função 'menu()', o usuário poderá escolher entre
# uma nova tentativa ou encerrar o jogo.
def menu():
    print('Deseja tentar novamente?')
    # Utilizei a estrutura 'try' para exibir mensagem de
    # erro caso o usuário escreva um valor diferente de
    # inteiro.
    try:
        opcao_menu = int(input('1 - Sim    2 - Não'))
        if opcao_menu == 1:
            primeirafase()
        elif opcao_menu == 2:
            # Com a função 'quit()', o programa é encerrado
            print('Encerrando...')
            quit()
        else:
            print('Oops! Opção inválida, tente novamente...')
            menu()
    except ValueError:
        print('Oops! Opção inválida, tente novamente...')
        menu()


# Função que exibe mensagem quando o usuário passa para a próxima fase:
def proximafase():
    print('\nCorreto! Você foi para a próxima fase!')


# função que termina o programa se o usuário perde
def perdeu():
    destaque('GAME OVER')
    print('Você perdeu!')
    menu()


def venceu():
    destaque('Parabéns')
    destaque('Você venceu o jogo!!!')
    # Aqui não foi necessário chamar a função 'sys.exit()',
    # porque o programa é procedural. Como não utilizei
    # estruturas de repetição (while e for) no programa
    # principal, o mesmo será encerrado automaticamente
    # após a última instrução.


# A função 'posicoes' exibe a estrutura de lista com as posições na tela
# desenho do gato em ANSII ART
# titulo do jogo
# para descrever as listas na tela usei o slice na mesma lista
def posicoes():
    print('                       []=++-')
    print('                      _II__|')
    print('                     [[__] |')
    print('    _________________|| |___')
    print('   /^^^^^^,-.^^^^^^^\|____|^^^\ ')
    print("  /   ___________              \ ")
    print(' /   /           \              \ ')
    print('/___/_ _ _ _ _ _ _\______________\ ')
    print('|=   ||/\|   |^^||`-`=|_|_|_|_|=|')
    print('|= = ||)(|   |__||= ==|_|_|_|_|=|')
    print('|= ==|´´´´   ````| = =____= =_==|')
    print('|== =| __     __ |= =| [] | |^|=|')
    print('|= ==||/\|   |==||== | o|=|_| | |')
    print('|== =||)(|   |  || = | == | == =|')
    print('|= ==|´´´´   ````|== |____|= = =|')
    print("mmmmm|___________|mmm------ mmmm|")
    print(' ')
    print('        |\_/|        D\___/| ')
    print('        (0_0)         (0_o)')
    print('       ==(Y)==         (V)')
    print('------(u)---(u)----oOo--U--oOo--')
    print('       HOTEL DOS ANIMAIS')
    print('_______|_______|_______|_______|')
    print('Especificando posição:')
    lista = [1, 2, 3, 4, 5, 6, 7, 8]
    print(lista[:4])
    print(lista[4:], '\n')
    for letra, hospede in dicio_hospedes.items():
        print(f'{letra} - {hospede}')


# Criei uma função para cada fase do jogo, criando um
# padrão de encadeamento if e else que executarão as
# funções 'perdeu()', 'proximafase()' e 'venceu()',
# dependendo se as respostas do jogador estiverem certas
# ou não.
# Também utilizei a estrutura 'try' para exibir mensagem de erro
# quando o usuário inserir um valor diferente de inteiro.
def primeirafase():
    destaque('Fase 1')
    print('Escolha onde deseja alocar o RATO e o GATO'
          '\nna seguinte matriz que representa os quartos:')
    print('[#]  [#]  [_]  [G]\n[R]  [_]  [#]  [#]\n')
    try:
        posicao_rato = int(input('Escreva a posição onde deseja alocar o RATO: '))
        posicao_gato = int(input('Escreva a posição onde deseja alocar o GATO: '))
        if posicao_rato != 6:
            perdeu()
        elif posicao_gato != 3:
            perdeu()
        else:
            proximafase()
    except ValueError:
        print('Oops! Opção inválida...')
        menu()


def segundafase():
    destaque('Fase 2')
    print('Você deverá alocar CÃO, CÃO e o OSSO'
          '\nna seguinte matriz que representa os quartos:')
    print('[_]  [#]  [#]  [#]\n[#]  [C]  [_]  [_]\n')
    try:
        posicao_cao1 = int(input('Escreva a posição onde deseja alocar o 1º CÃO: '))
        posicao_cao2 = int(input('Escreva a posição onde deseja alocar o 2º CÃO: '))
        posicao_osso = int(input('Escreva a posição onde deseja alocar o OSSO: '))
        if posicao_osso == 1:
            if posicao_cao1 == 7 or posicao_cao1 == 8:
                if posicao_cao2 == 7 or posicao_cao2 == 8:
                    proximafase()
        else:
            perdeu()
    except ValueError:
        print('Oops! Opção inválida...')
        menu()


def terceirafase():
    destaque('Fase 3')
    print('Você deverá alocar GATO, RATO e o OSSO'
          '\nna seguinte matriz que representa os quartos:')
    print('[_]  [#]  [#]  [#]\n[_]  [G]  [_]  [#]\n')
    try:
        posicao_gato = int(input('Escreva a posição onde deseja alocar o GATO: '))
        posicao_rato = int(input('Escreva a posição onde deseja alocar o RATO: '))
        posicao_osso = int(input('Escreva a posição onde deseja alocar o OSSO: '))
        if posicao_gato != 7:
            perdeu()
        elif posicao_rato != 1:
            perdeu()
        elif posicao_osso != 5:
            perdeu()
        else:
            proximafase()
    except ValueError:
        print('Oops! Opção inválida...')
        menu()


def quartafase():
    destaque('Fase 4')
    print('Você deverá alocar QUEIJO, QUEIJO e o OSSO'
          '\nna seguinte matriz que representa os quartos:')
    print('[_]  [_]  [_]  [#]\n[#]  [R]  [#]  [#]\n')
    try:
        posicao_queijo1 = int(input('Escreva a posição onde deseja alocar o 1º QUEIJO: '))
        posicao_queijo2 = int(input('Escreva a posição onde deseja alocar o 2º QUEIJO: '))
        posicao_osso = int(input('Escreva a posição onde deseja alocar o OSSO: '))
        if posicao_osso == 2:
            if posicao_queijo1 == 1 or posicao_queijo1 == 3:
                if posicao_queijo2 == 1 or posicao_queijo2 == 3:
                    venceu()
        else:
            perdeu()
    except ValueError:
        print('Oops! Opção inválida...')
        menu()


# Programa principal
posicoes()
primeirafase()
segundafase()
terceirafase()
quartafase()
