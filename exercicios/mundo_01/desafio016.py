#  FAÇA UM PROGRAMA QUE LEIA O COMPRIMENTO DO CATETO OPOSTO E DO CATETO ADJACENTE DE UM TRIANGULO RETANGULO, CALCULE E MOSTRE O COMPRIMENTO DA HIPOTENUSA
from math import sqrt, pow

cateto_oposto = int(input("informe o comprimento do cateto oposto "))
cateto_adjacente = int(input("informe o comprimento do cateto adjacente "))
hipotenusa = sqrt((pow(cateto_oposto,2) + pow(cateto_adjacente, 2)))

print(f'a hipotenusa do triangulo e igual a {hipotenusa:.1f}cm')