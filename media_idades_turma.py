# Exercício proposto: um programa que peça para n pessoas a sua idade,
# ao final o programa devera verificar se a média de idade da turma varia
# entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem,
# adulta ou idosa, conforme a média calculada.

idades_turma = []
numero_alunos = int(input("Quandos alunos há na turma?"))
for i in range(0, numero_alunos, 1):
    nome = input("Qual seu nome?")
    idade = int(input("Olá, {}! Escreva a sua idade: " .format(nome)))
    idades_turma.append(idade)
media = sum(idades_turma)/numero_alunos
if media > 60:
    print("A turma é idosa e possui idade média de {} anos" .format(media))
elif 26 <= media <= 60:
    print("A turma é adulta e possui idade média de {} anos" .format(media))
else:
    print("A turma é jovem e possui idade média de {} anos" .format(media))
