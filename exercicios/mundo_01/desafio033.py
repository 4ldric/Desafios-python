# ESCREVA UM PROGRAMA QUE PERGUNTE O SALARIO DE UM FUNCIONARIO E CALCUE O VALOR DO SEU AUMENTO. PARA SALARIOS SUPERIORES A R$ 1.250 CALCUE UM AUMENTO DE 10%, PARA INFERIORES OU IGUAIS O AUMENTO E DE 15%

salario = float(input('informe seu salario: '))
desconto = 0

if salario > 1250:
    desconto = salario * 1.10
    print(f'seu novo salario sera R${desconto:.2f}')
else:
    desconto = salario * 1.15
    print(f'seu novo salario sera R${desconto:.2f}')


#RESOLUÇÂO PROFESSOR

money = float(input('qual e o salario? '))

if money <= 1250:
    novo = money + (money * 15 / 100)
else:
    novo = money + (money * 10 / 100)
print(f'Quem ganhava R${money:.2f} passa a ganhar R${novo:.2f}')