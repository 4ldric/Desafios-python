#  CRIE UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE SETE PESSOAS. NO FINAL MOSTRE QUANTAS PESSOAS AINDA NAO ATINGIRAM A MAIORIDADE E QUANTOS JA SAO MAIORES
import datetime

maiores = []
menores = []
data_atual = datetime.date.today().year

for pessoa in range(7):
    ano = int(input('informe o ano do nascimento: '))
    idade = data_atual - ano
    if idade >= 18:
        maiores.append(idade)
    else:
        menores.append(idade)

print("Maiores de idade:", len(maiores))
print("Menores de idade:", len(menores))
