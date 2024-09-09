# FAÇA UM PROGRAMA QUE LEIA A LARGURA E A ALTURA DE UMA PAREDE EM METRO, CALCULE A SUA AREA E A QUANTIDADE DE TINTA NECESSARIA PARA PINTA-LA, SABENDO QUE A CADA LITRO DE TINTA, PINTA UMA AREA DE 2M².

largura = int(input("informe a largura da parede: "))
altura = int(input("informe a altura da parede: "))
area = largura * altura
cobertura_litro = 2
quantidade_necessaria= area // cobertura_litro

print(f'serao necessarios {quantidade_necessaria} litros de tinta para pintar {area}m²')