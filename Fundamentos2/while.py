#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
loop for usando o range que define quantidade valores
"""
numero_da_sorte = 0

while numero_da_sorte != 33:
    numero_da_sorte = int(input("Digite um numero da sorte: "))
    if numero_da_sorte == 33:
        print("Voce acertou, seu premio eh de R$1000,00 " '\n')
        break
    else:
        print("Voce errou nao recebeu nenhum valor" '\n')

print("Fim da sorte!")
