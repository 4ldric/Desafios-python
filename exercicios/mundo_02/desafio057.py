# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = input("Digite seu sexo [M/F]: ").lower()[0]
sair = True
while sair:
    if sexo in 'mf':
        print(f"Sexo {sexo.upper()} registrado com sucesso")
        sair = False
    else:
        sexo = input("Dados invalidos, informe seu sexo corretamente: ").lower()[0]
        
    

