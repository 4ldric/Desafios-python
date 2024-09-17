# FAÇA UM PROGRAMA QUE LEIA UM ANO QUALQUER E MOSTRE SE ELE  E BISSEXTO.

ano = int(input('Digite o ano atual: '))

if ano % 4 == 0:
    print(f'{ano} e um ano bissexto')
else:
    print(f'{ano} nao e um ano bissexto')


#RESOLUÇÃO PROFESSOR
from datetime import date # modulo de datas

year = int(input('que ano quer analisar? '))

if year == 0:
    year = date.today().year  #Retornar o ano atual de acordo com a data da maquina local

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f'{ano} e um ano bissexto')
else:
    print(f'{ano} nao e um ano bissexto')
