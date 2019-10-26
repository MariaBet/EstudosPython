#!/usr/bin/python3
# -*- coding: utf-8 -*-


print('============viagem de carro=======================')

distancia = float(input("Qual a distancia em KM?:  "))
velocidade = float(input("Qual a velocidade media qe você vai percorrer?:"))

tempo = distancia / velocidade

print('\n')
print("O tempo gasto em horas da viagem é: ", tempo, "horas")
