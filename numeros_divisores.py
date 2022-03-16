x = int(input("Escreva um número: "))
contador = 0
divisores = []
for i in range(1, x, 1):
    if x % i == 0:
        contador += 1
        divisores.append(i)
if contador > 2:
    print("{} não é um número primo" .format(x))
    print("{} é divisível por {} números".format(x, contador))
    print("Os números divisores de {} são {}".format(x, divisores[:]))
else:
    print("{} é um número primo" .format(x))
