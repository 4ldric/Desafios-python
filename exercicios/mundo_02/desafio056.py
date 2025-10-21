# DESENVOLVA UM PROGRAMA QUE LEIA O NOME, IDADE E SEXO DE 4 PESSOAS. NO FINAL DO PROGRAMA, MOSTRE:
#A MEDIA DE IDADE DO GRUPO
#QUAL E O NOME DO HOMEM MAIS VELHO
#QUANTAS MULHERES TEM MENOS DE 20 ANOS

idades = []
pessoas = []
homem_velho = None
mulheres = []

for pessoa in range(1,5):
    nome = input("Informe seu nome: ")
    idade = int(input("Informe sua idade: "))
    sexo = input("DIgite seu genero [F/M]: ").lower()
    idades.append(idade)
    pessoas.append({
        "nome": nome,
        "idade": idade,
        "sexo": sexo
    })

media_idades = sum(idades) / len(idades)
idades.sort(reverse=True)
maior_idade = idades[0]

for pessoa in pessoas:
    if pessoa["idade"] == maior_idade and pessoa["sexo"] == "m":
        homem_velho = pessoa
    if pessoa["sexo"] == "f" and pessoa["idade"] < 20:
        mulheres.append(pessoa)


if mulheres == []:
    mensagem = "não há mulheres "
elif len(mulheres) > 1:
    mensagem = f"há {len(mulheres)} mulheres"
else:
    mensagem = f"há {len(mulheres)} mulher"

print(f'A media de idade do grupo e: {media_idades}\nO homem mais velho do grupo e o {homem_velho['nome']} com {homem_velho['idade']} anos\nE {mensagem} abaixo de 20 anos')
