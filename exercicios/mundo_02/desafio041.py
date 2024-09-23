# A CONFEDERAÇÃO NACIONAL DE NATAÇAO PRECISA DE UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE UM ATLETA E MOSTRE  SUA CATEGORIA,
# DE ACORDO COM A IDADE. ATE 9 ANOS: MIRIM, ATE 14: INFANTIL, ATE 19: JUNIOR, ATE 20: SENIOR E ACIMA: MASTER
from datetime import date

ano = int(input('Informe seu ano de nascimento: '))
idade = date.today().year - ano

if idade <= 9:
    print('voce esta classificado como mirim')
elif idade <= 14:
    print('voce esta classificado como infantil')
elif idade <= 19:
    print('voce esta classificado como junior')
elif idade == 20:
    print('voce esta classificado como senior')
else: 
    print('voce esta classificado como master')






