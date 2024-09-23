# FAÇA UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO E INFORME, DE ACORDO COM SUA IDADE...
# SE ELE AINDA VAI SE ALISTAR AO SERVIÇO., SE E A HORA DE SE ALISTAR OU SE JA PASSOU DO TEMPO DO ALISTAMENTO
# O PROGRAMA TAMBEM DEVERA MOSTAR O TEMPO QUE FALTA OU QUE PASSOU DO PRAZO
from datetime import date

nascimento = int(input('informe seu ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - nascimento
tempo_restante = 0

if idade < 18:
    tempo_restante = 18 - idade
    print(f'Voce ainda nao esta elegivel para se alistar ao serviço. \nvoce podera se alistar daqui {tempo_restante} anos')
elif idade > 18:
    tempo_restante = idade - 18 
    alistamento = ano_atual - tempo_restante 
    print(f'Seu alistamento ocorreu no ano de {alistamento}, voce ja passou do prazo de alistamento a {tempo_restante} anos, procure uma junta militar de imediato!!')
else:
    print('Voce ja esta apto para continuar com o alistamento, diriga-se a uma junta militar!')