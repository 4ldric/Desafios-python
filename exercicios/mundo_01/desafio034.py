# DESENVOLVA UM PROGRAMA QUE LEIA O COMPRIMENTO DE TRES RETAS E DIGA AO USUARIOS SE ELAS PODEM OU NAO FORMAR UM TRIANGULO

lado1 = int(input('informe a primeira reta: '))
lado2 = int(input('informe a segunda reta: '))
lado3 = int(input('informe a terceira e maior reta: '))

condicao = lado1 + lado2

if condicao > lado3:
    print('As tres retas podem formar um triangulo')
else:
    print(' as retas nao podem formar um triangulo')


# RESOLUÇÃO PROFESSOR

print('-=' * 20)
print('Analisador de triangulo')
print('-=' * 20)

r1 = float(input('primeiro segmento:'))
r2 = float(input('segundo segmento:'))
r3 = float(input('terceiro segmento:'))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As tres retas podem formar um triangulo')
else:
    print(' as retas nao podem formar um triangulo')
