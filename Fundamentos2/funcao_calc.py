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
    print('O resto da divisão não esta ok é.: ', n1 % n2)


""" Menu """
opera = 0
while opera != 'e':
    opera = input('''Escolha a operação:
    + p/ Soma
    - p/ Subtracao
    / p/ Divisão
    * p/ Multiplicacao
    r p/ Resto da divisao
    e p/ encerrar
    \n''')
    if opera == 'e':
        print("Encerrado")
        break

    n1 = int(input('Digite o primeiro valor.: '))
    n2 = int(input('Digite o segundo valor.: '))

    """ Chamando as funções """
    if opera == '+':
        soma(n1, n2)
        print('\n')

    elif opera == '-':
        subtracao(n1, n2)
        print('\n')

    elif opera == '*':
        multiplicacao(n1, n2)
        print('\n')

    elif opera == '/':
        divisao(n1, n2)
        print('\n')

    elif opera == 'r':
        resto(n1, n2)
        print('\n')

    if opera not in 'e':
        print("Calculo Feito")
        break

    else:
        print('Erro! Por favor digite uma opção valida na proxima execução')
