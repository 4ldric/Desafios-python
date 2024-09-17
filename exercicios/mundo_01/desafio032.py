#FAÇA UM PROGRAMA QUE LEIA TRES NUMEROS E MOSTRE QUAL E O MAIOR E QUAL E O MENOR.
#RESOLUÇÂO PROFESSOR

a = int(input('digite um numero: '))
b = int(input('digite um numero: '))
c = int(input('digite um numero: '))

#verificando o menor
menor = a

if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
#verificando o maior
maior = a

if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print(f'o menor valor digitado foi {menor}')
print(f'o maior valor digitado foi {maior}')
