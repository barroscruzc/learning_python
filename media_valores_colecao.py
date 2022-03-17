# Exercício proposto: Faça um programa que calcule o valor total investido
# por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles.
# O usuário deverá informar a quantidade de CDs e o valor para em cada um.

def calcula_media(a,b):  # calcula a média de um valor, dividindo o total(a) pelo número de itens(b)
    media = a/b
    return media


total_cds = []
num_cds = int(input("Quantidade de itens existentes na coleção: \n"))

for i in range(1, num_cds+1, 1):
    name = "0" + str(i)
    valor_cd = float(input("Valor gasto do CD nº {} \n" .format(name)))
    total_cds.append(valor_cd)
media = calcula_media(sum(total_cds), num_cds)
print("A coleção de CDS possui o valor total de R$ {}, ".format(sum(total_cds)), end='')
print(f"com o valor médio de R${round(media, 2)} por CD.")
