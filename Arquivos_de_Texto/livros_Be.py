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
        print('0  - Sair\n')

        opcao = input('Entre com o número da opção: ')
        print()

        if (opcao == '1'):
            ver()
        elif (opcao == '2'):
            adcionar()
        elif (opcao == '0'):
            sys.exit(0)
        else:
            print('Opção Inválida')


def existe():
    if os.path.isfile('TestesPython/listadeLivros.txt'):
        return 'TestesPython/listasdeLivros.txt'
    else:
        return ' '


def ver():
    arq = existe()
    if not arq:
        input("O arquivo listasdeLivros.txt ainda não foi criado, tecle enter para continuar")
        return
main()
