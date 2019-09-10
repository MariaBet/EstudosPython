#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Lista
carros = []

# Input de elementos
nome = input("Digite o modelo do carro: ")

while nome != '0':
    carros.append(nome)
    carros.sort()
    print(carros)
    nome = input("Digite o modelo do carro: ")
