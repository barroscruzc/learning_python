# Enunciado da questão: Uma sequência de números é tal que seus 4 primeiros termos são:
# T1=5    T2=13    T3=24    T4=38
#
# Oberva-se que:
# 13=5+8
# 24=5+8+11
# 38=5+8+11+14
#
# Conclui-se, então, que o 30º. termo(T30) dessa sequência é:


x = 5  # Termo inicial da 1a. sequência
seq_1 = [5] # 1a. sequência: determina os valores que, se somados, resultam nos termos da 2a. sequência
contador = 1

while contador <= 30:
    x = x + 3  # Cada termo da 1a. sequência é igual ao anterior + 3
    seq_1.append(x)  # Insere o termo na lista da 1a. sequência
    contador += 1

seq_2 = []
for i in range(0, len(seq_1)-1, 1):
    a = seq_1[i]+sum(seq_1[0:i])
    seq_2.append(a)

print("O {}º termo dessa sequência é:{}" .format(len(seq_2), seq_2[29]))
print("A sequência completa é: {}" .format(seq_2))
print("A soma de todos os termos da sequência é {}" .format(sum(seq_2)))
