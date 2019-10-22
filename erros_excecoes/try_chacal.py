#!/usr/bin/python
# -*- coding: utf-8 -*-

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
