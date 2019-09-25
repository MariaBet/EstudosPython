#!/usr/bin/python3
# -*- coding: utf-8 -*-

""" Funções """
def soma(n1, n2):
    print('A soma é.: ', n1 + n2)

def subtracao(n1, n2):
    print('A subtração é.: ', n1 - n2)

def multiplicacao(n1, n2):
    print('A multiplicação é.: ', n1 * n2)

def divisao(n1, n2):
    print('A divisao é.: ', n1 / n2)

def resto(n1, n2):
    print('O resto da divisão é.: ', n1 % n2)


""" Inputs """
n1 = int(input('Digite o primeiro valor.: '))
n2 = int(input('Digite o segundo valor.: '))
print('\n')


""" Chamando as funções """
soma(n1, n2)
subtracao(n1, n2)
multiplicacao(n1, n2)
divisao(n1, n2)
resto(n1, n2)
