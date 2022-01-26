#  Primeiro criei uma função 'modifica' que irá
# modificar a string a ser recebida na variável 'nome'
def modifica(nome):
    #  Nesta função 'for', para cada caracter da
    #  string contida em 'nome', o programa irá avaliar
    # se foram preenchidas as condições das seguintes
    # estruturas condicionais:
    for letra in nome:
        #  Dentro da string 'nome, caso o caracter contido
        #  no índice correspondente ao valor inteiro de 'letra'
        #  seja igual a uma das vogais abaixo indicadas (ainda
        #  que sejam maiúsculas, minústculas e/ou acentuadas),
        #  o programa irá imprimir o símbolo correspondente
        #  na tabela do enunciado.
        if letra == 'a' or letra == 'ã' or letra == 'A' or letra == 'Ã':
            print('@', end='')
        #  As próximas três estruturas condicionais serão
        #  'elif', pois assim o computador só avaliará suas condições
        #  de validade CASO a estrutura anterior seja FALSA. Equivale a
        #  utilizar 'if' + 'else', mas por uma questão de legibilidade
        #  optei por usar 'elif', pois desse modo o código torna-se
        #  mais "limpo".
        elif letra == 'e' or letra == 'é' or letra == 'E' or letra == 'É':
            print('&', end='')
        elif letra == 'i' or letra == 'í' or letra == 'I' or letra == 'Í':
            print('!', end='')
        elif letra == 'o' or letra == 'õ' or letra == 'ó' or letra == 'ô':
            print('#', end='')
        elif letra == 'O' or letra == 'Õ' or letra == 'Ó' or letra == 'Ô':
            print('#', end='')
        elif letra == 'u' or letra == 'ú' or letra == 'U' or letra == 'Ú':
            print('*', end='')
        #  Por último, utilizei 'else', pois assim serão incluídos
        #  quaisquer caracteres que não sejam vogais.
        else:
            #  Outros caracteres serão impressos na tela normalmente:
            print(letra, end='')


#  Programa principal:
#  O loop abaixo seria infinito, mas será interrompido pelo
#  comando 'break' ao final do código, caso o usuário escolha
#  a opção de encerrar o programa.
while True:
    nome = input('Escreva seu nome:')
#  A próxima linha chama a função 'modifica' para alterar
#  o nome inserido de acordo com a tabela do enunciado:
    modifica(nome)
    fim = input('\nDeseja continuar?   0 - Não   1 - Sim')
    if not fim:
        break
print('Encerrando...')
