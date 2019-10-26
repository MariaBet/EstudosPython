#!/usr/bin/python3
# -*- coding: utf-8 -*-



print('=================Mercadoria=======================')

mercadoria = float(input("Digite o preço da mercadoria: "))
desconto = float(input("Digite o valor do desconto da mercadoria: "))

desc = ((mercadoria * desconto) / 100 )

print("O valor do desconto é: ", desc)

pre = mercadoria - desc

print("O valor a pagar é: ", pre)
