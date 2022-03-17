def calcula_media(a,b):
    media = a/b
    return media

def valida(x):
    while x > 40 or x < 1:
        print("Ops! As turmas não podem ter mais de 40 alunos.")
        x = int(input("Número de alunos da turma:"))


total_alunos = []
nomes_turmas = []
num_turmas = int(input("Quantidade de turmas existentes: "))

for i in range(1, num_turmas+1, 1):
    name = "Turma 0" + str(i)
    print(name)
    num_alunos = int(input("Número de alunos da turma {}: \n" .format(name)))
    valida(num_alunos)
    total_alunos.append(num_alunos)

print("A escola possui a média de {} alunos por turma." .format(calcula_media(sum(total_alunos), num_turmas)))


