#!/usr/bin/python
# -*- coding: utf-8 -*-

<<<<<<< HEAD
x = 12
y = 0

try:
    z = x/0
except ZeroDivisionError:
    print('Nenhum valor pode ser dividido por zero\n')


try:
    n1 = int(input('Primeiro valor inteiro.: '))
    n2 = int(input('Segundo valor inteiro.: '))
except ValueError:
    print('Por favor! Digite um valor INTEIRO!')
=======

'''try - bloco permite testar um bloco d codigo quanto a erros
except bloco permite lidar com o erro
finally excutar o codigo indepente do resultado do try e Exception'''


try:
    print(n)
    print("exception")
>>>>>>> f5b23209012bf7d2d298cd07d0aafcaca1131bbb
