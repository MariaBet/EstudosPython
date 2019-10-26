#!/usr/bin/python3
# -*- coding: utf-8 -*-

print("=================================================")

salario = float(input("Digite o valor do salário: "))
aumento =float(input("Digite a % do aumento do salario: "))

novoSalario = salario + ((salario * aumento) / 100 )

print("O valor do novo aumento do salário é: ", novoSalario)
