#!/usr/bin/python3
# -*- coding: utf-8 -*-

""" Variavel Global """


# Variavel simples
num = 10

# Criando minha função
def my_fun():
    global num #Aqui definimos que a variavel é global
    num = 20 #Esta variavel global recebe um valor
    #print(num) #Aqui é impresso o valor da variavel global


# Este print é da variavel comum, a função ainda não foi chamada. Portanto
# a global ainda não existe.
print("O valor comum de NUM é.: ", num, '\n')

# Chamada a função, a partir de agora a variavel global existe.
my_fun()
print("O valor da variavel apenas dentro da função NUM é.: ", num, '\n' )

# Impressão da variavel
print("O valor de NUM agora sendo global e sobrepondo é.: ", num, '\n')
