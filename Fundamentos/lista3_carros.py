#!/usr/bin/python3
# -*- coding: utf-8 -*-

carros = []
nome = input("Digite o modelo do carro: ")

# Enquanto o nome do carro for diferente de zero
# ele vai continuar incluindo elementos
# até que a string 0 seja digitada
while nome != '0':
    carros.append(nome)
    carros.sort()
    print(carros)
    nome = input("Digite o modelo do carro: ")
