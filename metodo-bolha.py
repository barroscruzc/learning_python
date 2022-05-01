#  estrutura de dados - metodo bolha
#  recebe uma sequencia de valores e os ordena de forma crescente

var_aux = 0
vetor = []

for a in range(0, 10, 1):
    print("Número ", a+1)
    d = int(input(''))
    vetor.append(d)

for b in range(0, 10, 1):
    for c in range(0, 10, 1):
        if vetor[c] > vetor[b]:
            var_aux = vetor[b]
            vetor[b] = vetor[c]
            vetor[c] = var_aux

print(vetor)