# A estrutura de repetição abaixo ('while True') não possui condição
# válida para interromper sua execução. Esse loop, que seria infinito,
# será interrompido pelo comando 'break' ao final do código, caso
# o usuário escolha a opção de encerrar o programa.
while True:
    nome_crianca = input('Nome da criança: ')
    idade = int(input('Idade: '))
    lvl_ensino = ' '
    #  Nas próximas linhas utilizo as estruturas condicionais para
    #  determinar o valor da variável 'lvl_ensino'. Assim, o nível
    #  de ensino a ser impresso na tela para o usuário corresponderá
    #  à faixa etária correspondente.
    if idade >= 1 and idade <= 5:
        lvl_ensino = 'Ensino Infantil'
    #  As próximas três estruturas condicionais utilizadas serão
    #  'elif', pois assim o computador só avaliará suas condições
    #  de validade CASO a estrutura anterior seja FALSA. Equivale a
    #  utilizar 'if' + 'else', mas por uma questão de legibilidade
    #  optei por usar 'elif', pois desse modo o código torna-se
    #  mais "limpo".
    elif idade >= 6 and idade <= 10:
        lvl_ensino = 'Ensino Fundamental I'
    elif idade >= 11 and idade <= 14:
        lvl_ensino = 'Ensino Fundamental II'
    elif idade >= 15:
        lvl_ensino = 'Ensino Médio'
    #  Caso a idade receba um valor inferior a 1, que é a idade
    #  mínima na faixa etária para matrícula, o programa avisará
    #  o erro ao usuário.
    else:
        print('Valor inválido!')
        print('A idade mínima para matrícula é 1 ano de idade.')
    #  Na próxima estrutura condicional, utilizei o 'if' em vez
    #  de 'elif' porque para mostrar o nível de ensino do aluno é
    #  necessário primeiro verificar se a idade inserida é válida.
    #  O programa NÃO atenderá ao próximo comando 'print' caso o
    #  valor para idade seja INVÁLIDO (menor do que 1) e continuará
    #  para a próxima instrução.
    if idade >= 1:
        #  Utilizei a instrução '.format' a fim de manipular a string
        #  para utilizar os dados informados pelo usuário e contidos
        #  nas variáveis 'nome_crianca', 'idade' e 'lvl_ensino' e
        #  mostrar corretamente o nível de ensino correspondente
        #  à idade da criança.
        print('O(a) aluno(a) {} tem {} anos e está no {}' .format(nome_crianca, idade, lvl_ensino))
    fim = int(input('Deseja continuar?  0 - Não    1 - Sim\n'))
    if not fim:
        break
print('Encerrando programa...')
