#  FAÇA UM PROGRAMA QUE LEIA O COMPRIMENTO DO CATETO OPOSTO E DO CATETO ADJACENTE DE UM TRIANGULO RETANGULO, CALCULE E MOSTRE O COMPRIMENTO DA HIPOTENUSA
from math import sqrt, pow

cateto_oposto = float(input("informe o comprimento do cateto oposto "))
cateto_adjacente = float(input("informe o comprimento do cateto adjacente "))
hipotenusa = sqrt((pow(cateto_oposto, 2) + pow(cateto_adjacente, 2)))

print(f'a hipotenusa do triangulo e igual a {hipotenusa:.2f}cm')


# RESOLUÇÃO PROFESSOR

from math import hypot

co = float(input("informe o comprimento do cateto oposto "))
ca = float(input("informe o comprimento do cateto adjacente "))
hi = hypot(co, ca)

print(f'a hipotenusa do triangulo e igual a {hi:.2f}cm')
