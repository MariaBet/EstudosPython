#!/usr/bin/python3
# -*- coding: utf-8 -*-

""" Funções """
def soma(n1, n2):
    return n1+n2

def subtracao(n1, n2):
    return n1-n2

def multiplicacao(n1, n2):
    return n1*n2

def divisao(n1, n2):
    return n1/n2

def resto(n1, n2):
    return n1%n2


""" Menu """
opera = 0
while opera != 'e':
    opera = input('''Escolha a operação:
    + p/ Soma
    - p/ Subtracao
    / p/ Divisão
    * p/ Multiplicacao
    r p/ Resto da divisao
    e p/ encerrar programa
    \n''')

    # Se a opção escolhida for E, o programa encerra
    # sem passar pelos inputs de valores
    if opera == 'e':
        print("Encerrado")
        break

    n1 = int(input('Digite o primeiro valor.: '))
    n2 = int(input('Digite o segundo valor.: '))

    """ Chamando as funções """
    if opera == '+':
        print('A soma dos valores é.: ',soma(n1, n2))
        print('\n')

    elif opera == '-':
        print('A subtração dos valores é.: ',subtracao(n1, n2))
        print('\n')

    elif opera == '*':
        print('A multiplicação dos valores é.: ',multiplicacao(n1, n2))
        print('\n')

    elif opera == '/':
        print('A divisão dos valores é.: ',divisao(n1, n2))
        print('\n')

    elif opera == 'r':
        print('O resto da divisão dos valores é.: ',resto(n1, n2))
        print('\n')

    if opera not in 'e':
        print("Calculo Feito")
        break

    else:
        print('Erro! Por favor digite uma opção valida na proxima execução')
