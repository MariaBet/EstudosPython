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


def agenda(n): # siginifica argumento
    a, b = 0, 2
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()


while True:
    m = int(input('Sequencia ate quanto?: '))
    agenda(m)
    break
