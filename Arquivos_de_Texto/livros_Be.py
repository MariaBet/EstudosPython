#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import sys


def main():
    print('Programa para administrar sua lista de livros')
    print()

    while True:
        print()
        print('Escolha uma das opções abaixo\n')
        print('1 - Ver a lista')
        print('2 - Adicionar livros na lista')
        print('3 - Excluir Livros na lista')
        print('0 - Sair\n')

        opcao = input('Entre com o número da opção: ')
        print()

        if (opcao == '1'):
            ver()
        elif (opcao == '2'):
            adicionar()
        elif (opcao == '0'):
            sys.exit(0)
        else:
            print('Opção Inválida')


def existe():
    if os.path.isfile('listadeLivros.txt'):
        return 'listasdeLivros.txt'
    else:
        return ' '


def ver():
    arq = existe()
    #if not arq:
    #    input("O arquivo listasdeLivros.txt ainda não foi criado, tecle enter para continuar")
    #    return
    print("Lista de Livros: ")
    print("Tecle enter " '\n')
    arq = open('listasdeLivros.txt', 'r')
    livros = arq.readlines()

def adicionar():
    livros = []

    opcao = 'a'
    arq = existe()

    if not arq:
        opcao = "w"


    print("Digite o nome do Livro e fim para sair: ")
    arq = open('listadeLivros.txt', 'a')
    livros = 0
    while True:
        livro = input()
        if livros != '0':
            break
    arq.write(livro)
    arq.write('\n')

    arq.close()
    print('Livro Maravilhoso')


main()
