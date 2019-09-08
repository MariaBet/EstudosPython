#!/usr/bin/python
# -*- coding: utf-8 -*-

# Declaracao de variaveis
n1 = float(input('Digite a nota da prova: '))
n2 = float(input('Digite a nota do trabalho: '))
nota = n1 + n2

# Boolean True e False
if nota / 2 >= 5:
    situacao = True
    print(nota / 2)

else:
    situacao = False
    print(nota / 2)

print(situacao)
