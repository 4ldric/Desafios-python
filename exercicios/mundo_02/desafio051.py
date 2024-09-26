# DESENVOLVA UM PROGRAMA QUE LEIA O PRIMEIRO TERMO E A RAZAO DE UMA PROGESSAO ARITMETICA. NO FINAL, MOSTRE OS 10 PRIMEIROS TERMOS DESSA 
termo = int(input('informe o primeiro termo: '))
termo2 = int(input('informe outro termo: '))

for numero in range(0,5):
    razao = termo2 - termo
    termo += razao

    resultado = termo 

print(resultado)