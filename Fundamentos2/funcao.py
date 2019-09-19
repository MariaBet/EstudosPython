#!/usr/bin/python3
# -*- coding: utf-8 -*-


def cadastro():
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    print(nome, "Minha idade eh: ", idade, '\nMaravilha!!!\n')


cadastro()
cadastro()
cadastro()      # Chama a função 3 vezes, sem precisar digitar o codigo todo

# variavel local


def agenda(n):       # significa argumento
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b   # sequencia de fibonacci
    print('\n')


while True:
    m = int(input('Sequencia ate quanto?: '))
    agenda(m)
    break


# return
def soma(b, e):
    print("A soma eh: ")
    return b + e


print(soma(28, 33))
print(soma(-28, 33))


# trechos de codigos retirados do
# https://docs.python.org/3/tutorial/controlflow.html#defining-functions
