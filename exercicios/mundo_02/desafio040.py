# CRIE UM PROGRAMA QUE LEIA DUAS NOTAS E CALUCLE A MEDIA DO ALUNO, MOSTRANDO UMA MENSAGEM NO FINAL DE ACORDO COM A MEDIA
# MEDIA ABAIXO DE 5.0: REPROVADO
# MEDIA ENTRE 5.0 E 6.9: RECUPERAÇÃO
# MEDIA 7.0 OU SUPERIOR: APROVADO


nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))
media = (nota1 + nota2) / 2

if media < 5:
    print(f'Voce esta reprovado com nota {media}')
elif media < 6.9:
    print(f'Voce esta em recuperação com nota {media}')
else: 
    print(f'Parabens, voce foi aprovado com nota {media}')