# ESCREVA UMA LOGICA QUE LEIA O PESO E A ALTURA DE UMA PESSOA, CALCULE O IMC E MOSTRE SEU STATUS, DE ACORDO COM A TABELA
# ABAIXO DE 18.5: ABAIXO DO PESO 
# ENTRE 18.5 E 25: PESO IDEAL
# 25 ATE 30: SOBREPESO
# 30 A 40: OBESIDADE
# ACIMA DE 40: OBESIDADE MORBIDA

peso = int(input('informe seu peso '))
altura = float(input('informe sua altura '))
imc = peso / altura ** 2

if imc < 18:
    print(f'seu imc e {imc:.2f}: voce esta abaixo do peso!!')
elif imc < 25:
    print(f'seu imc e {imc:.2f}: voce esta no peso ideal')
elif imc < 30:
    print(f'seu imc e {imc:.2f}: voce esta com sobrepeso')
elif imc < 40:
    print(f'seu imc e {imc:.2f}: voce possui OBESIDADE')
else:
    print(f'seu imc e {imc:.2f}: va ao nutricionista urgente voce tem OBESIDADE MORBIDA')