notas = []
x = int(input("Escreva o número de notas a serem calculadas:"))
for i in range(0, x, 1):
    nova_nota = float(input("Digite a {}ª nota: " .format(i+1)))
    notas.append(nova_nota)
media = sum(notas[:])/x
print("A média do aluno é: {}" .format(media))
