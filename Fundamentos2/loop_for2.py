#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
loop for usando o range que define quantidade valores
"""
numero_da_sorte = 33
tentativas = 5

for tentativas in range(5):
    print("Tentativa: ", tentativas)
    numero_da_sorte = int(input("Digite um numero da sorte: "))
    if numero_da_sorte == 33:
        print("Voce acertou, seu premio eh de R$1000,00 " '\n')
        break
    elif numero_da_sorte != 33:
        print("Voce errou nao recebeu nenhum valor" '\n')

print("Fim da sorte!")


# parar o loop caso acerte o numero
