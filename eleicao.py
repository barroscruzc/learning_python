def porcentagem(x):  # calcula a porcentagem de votos recebida pelo candidato
    resultado = x * 100 / num_eleitores
    return resultado


urna = []
num_eleitores = int(input("Número de eleitores:"))  # total de votos a serem computados

for i in range(0, num_eleitores, 1):  # O programa recebe votos N vezes, conforme o número de eleitores
    voto = int(input("Você é o {}ª eleitor de hoje. \n"
                     "Escreva o número do candidato que deseja eleger: \n"
                     "1 - Felizberto\n"
                     "2 - Anselmo\n"
                     "3 - Maria\n"
                     .format(i + 1)))
    urna.append(voto)  # Adiciona à urna o número do candidato escolhido

candidato_1 = urna.count(1)  # conta quantas vezes o número do candidato aparece na urna
candidato_2 = urna.count(2)
candidato_3 = urna.count(3)
vencedor = ""
votos_vencedor = 0

# Aquele que possuir o maior número de votos será eleito
if candidato_1 > candidato_2 and candidato_1 > candidato_3:
    vencedor = "Felizberto"
    votos_vencedor = candidato_1
elif candidato_2 > candidato_1 and candidato_2 > candidato_3:
    vencedor = "Anselmo"
    votos_vencedor = candidato_2
elif candidato_3 > candidato_1 and candidato_3 > candidato_2:
    vencedor = "Maria"
    votos_vencedor = candidato_3
# Exibe o candidato eleito, o número de votos que ele recebeu e a respectiva porcentagem
print("{} foi eleito(a) com {} votos ({}%)!".format(vencedor, votos_vencedor, porcentagem(votos_vencedor)))

# Exibe o resultado geral da votação
print("Resultado:\n")
print("Total: {} votos".format(num_eleitores))
print("1 - Felizberto: {} votos ({}%)\n".format(candidato_1, porcentagem(candidato_1)))
print("2 - Anselmo: {} votos ({}%)\n".format(candidato_2, porcentagem(candidato_2)))
print("3 - Maria: {} votos ({}%)".format(candidato_3, porcentagem(candidato_3)))
