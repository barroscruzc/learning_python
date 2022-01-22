# Crie uma tupla preenchida com os 20 primeiros colocados da
# Tabela do Campeonato Brasileiro de Futebol,
# na ordem de colocação. Depois mostre:
# a) Apenas os 5 primeiros colocados.
# b) Os últimos 4 colocados da tabela.
# c) Uma lista com os times em ordem alfabética.
# d) Em que posição na tabela está o time da Chapecoense.
#
# Função 'linha' para melhorar a visibilidade e organização das informações impressas na tela
def linha():
    print('_' * 15)


# Tupla com os 20 times da série A 2021:
tabela = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Bragantino', 'Fluminense', 'America-MG', 'Atlético-GO', 'Santos', 'Ceará', 'Internacional', 'São Paulo', 'Athletico-PR', 'Cuiabá', 'Juventude', 'Grêmio', 'Bahia', 'Sport Recife', 'Chapecoense')
linha()
print('BRASILEIRÃO 2021\nTabela Série A:')
for a in range(0, 19, 1):  # Imprime todos os valores inseridos na tupla 'tabela'
    print(tabela[a])
linha()
print('Os 5 primeiros colocados:')
for i in range(0, 5, 1):
    print('{} em {}º lugar' .format(tabela[i], i+1))
linha()
print('Os 4 últimos colocados:')
for b in range(16, 20, 1):
    print('{} em {}º lugar'.format(tabela[b], b+1))
linha()
print('Os times da Série A em ordem alfabética:')
print(sorted(tabela))  # função 'sorted' organiza os itens em ordem alfabética
linha()
print('O time da Chapecoense está na {}ª posição' .format(tabela.index('Chapecoense')+1))
# A função 'index' indica o índice onde está localizado o elemento na tupla.
# Foi necessário acrescentar +1 porque o número de elementos da tupla != índice da tupla
# (índice inicia em 0).
