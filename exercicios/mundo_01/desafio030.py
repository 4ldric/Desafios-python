# Desenvolva um programa que pergunte a distancia de uma viagem em kM. calcule o preço da passagem, cobrando r$0,50 por km ára viagens de ate 200Km e R$ 0,45 para viagens mais longas

km = int(input('Digite o total de km da sua viagem: '))


if km <= 200:
    soma = km * 0.50
    print(f'o preço total da sua passagem e R${soma:.2f}')
else: 
    soma = km * 0.45
    print(f'o preço total da sua passagem e R${soma:.2f}')
