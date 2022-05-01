#  logica de programacao e algoritmos
#  tema: metodos e procedimentos


def verifica_triangulo():
    if (lado_a > lado_b + lado_c) or (lado_b > lado_a + lado_c) or (lado_a > lado_b + lado_c):
        return False
    else:
        return True


def tipo_triangulo():
    if (lado_a == lado_b) and (lado_b == lado_c):
        return "Equilátero"
    elif (lado_a == lado_b) or (lado_b == lado_c) or (lado_a == lado_c):
        return "Isósceles"
    else:
        return "Escaleno"


#  função principal


lado_a = int(input('Lado 1: '))
lado_b = int(input('Lado 2: '))
lado_c = int(input('Lado 3: '))
if not verifica_triangulo():
    print("Isto não é um triângulo")
else:
    resultado = tipo_triangulo()
    print('Isto é um triângulo {}.'.format(resultado))




