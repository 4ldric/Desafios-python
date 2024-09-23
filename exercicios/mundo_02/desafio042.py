#  REFAÇA O DESAFIO 034 DOS TRIANGULOS ACRESCENTANDO O RECURSO DE MOSTRAR QUE TIPO DE TRIANGULO SERA FORMADO:
# EQUILATERO: TODOS OS LADOS IGUAIS
# ISOSCELES: DOIS LADOS IGUAIS
# ESCALENO: TODOS OS LADOS DIFERENTES

# RESOLUÇÃO PROFESSOR

print('-=' * 20)
print('Analisador de triangulo')
print('-=' * 20)

r1 = float(input('primeiro segmento:'))
r2 = float(input('segundo segmento:'))
r3 = float(input('terceiro segmento:'))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As tres retas podem formar um triangulo', end = '')

    if r1 == r2 == r3:
        print(' EQUILATERO!')
    elif r1 != r2 and r1 != r3 and r2 != r3:
        print(' ESCALENO!')
    else:
        print(' ISOSCELES!')

else:
    print(' as retas nao podem formar um triangulo')
