# Faça um programa que leia algo e mostre na tela o seu tipo primitivo e todas as informações possiveis sobre ele

valor = input("Digite algo: ")

print("o tipo de dado e ", type(valor))
print("pode ser convertido em numero? ",valor.isnumeric())
print("e um texto? ", valor.isalpha())
print("so tem espaço?", valor.isspace())
print("o tipo e alfanumerico?", valor.isalnum())
