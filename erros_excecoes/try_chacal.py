#!/usr/bin/python
# -*- coding: utf-8 -*-


# Variaveis p/ teste do primeiro erro
x = 12
y = 0

# Todo codigo que pode haver erros, deve ser inserido dentro
# do bloco try
try:
    z = x/0

# E todo bloco try deve haver uma exceção ou finally para que
# o erro seja tratado ou ignorado
except ZeroDivisionError:
    print('Nenhum valor pode ser dividido por zero\n')


try:
    n1 = int(input('Primeiro valor inteiro.: '))
    n2 = int(input('Segundo valor inteiro.: '))
except ValueError:
    print('Por favor! Digite um valor INTEIRO!\n\n')

try:
    n1 = float(input('Primeiro valor flutuante.: '))
    n2 = float(input('Segundo valor flutuante.: '))
except ValueError:
    print('Por favor! Digite um valor FLUTUANTE, OU SEJA "NAO INTEIRO"'
    ' com VIRGULA ... ENTENDE USUARIO kkkkk!')
finally:
    print('Mesmo havendo erro, o finally sempre sera executado')
