#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Importação de modulos"""
import os
import sys
import time

### AQUI COMEÇA O PROGRAMA DE FATO
### AGUARDE 5 SEGUNDOS APOS A EXECUÇÃO DO PROGRAMA, PARA QUE SEJA
### REALIZADO UM CLEAR NA TELA


"""FUNÇÕES"""

""""Função Main"""
def main():
    print('Lista de filmes favoritos\n')

    while True:
        print('\nEscolha uma das opções abaixo\n')
        print('1 - Ver a lista')
        print('2 - Adicionar filmes na lista')
        print('3 - Excluir filmes da lista')
        print('0 - Sair\n')
        opcao = input('Entre com o número da opcao.: ')
        print()

        if (opcao == '1'):
            ver()
        elif (opcao == '2'):
            adicionar()
        elif (opcao == '3'):
            excluir()
        elif (opcao == '0'):
            sys.exit(0)
        else:
            print('Opcao inválida')



""""Função Visualizar Lista"""
def ver():
    # Usado a função path.isfile do modulo OS, para verificar
    # a existencia do arquivo de lista
    if os.path.isfile('filmes_chacal.txt') == True:

        print('Lista de filmes existente\n')

        # Abrir arquivo no modo leitura (r)
        arquivo = open('filmes_chacal.txt', 'r')
        # Lendo o conteudo do arquivo com a função read
        print(arquivo.read())

    else:
        print('A lista de filmes não existe, volte ao menu e escolha outra opção')


""""Função Adicionar Lista"""
def adicionar():
    if os.path.isfile('filmes_chacal.txt') == True:

        print('Lista de filmes existente\n')

        # Abrir arquivo no modo append (a)
        # O modo append preserva o conteudo existe do arquivo caso ele
        # já exista. Diferente do modo (w) que exclui o conteudo e adiciona
        # um novo conteudo.
        arquivo = open('filmes_chacal.txt', 'a')

        conteudo = '0'
        while conteudo != 'fim':
            conteudo = input('Digite o nome de um filme.: ')
            if conteudo == 'fim':
                break
            arquivo.write(conteudo)
            arquivo.write('\n')

        # Fechando arquivo p/ salvar
        arquivo.close()
        print('Filme adicionado com sucesso!')

    else:
        print('A lista de filmes não existe, adicione novos filmes e uma lista'
                'sera criada pra você!')

        arquivo = open('filmes_chacal.txt', 'w')

        conteudo = '0'
        while conteudo != 'fim':
            conteudo = input('Digite o nome de um filme.: ')
            if conteudo == 'fim':
                break

            arquivo.write('\n')

            # Fechando arquivo p/ salvar
            arquivo.close()
            print('Filme adicionado com sucesso!')


""""Função Excluir Lista"""
def excluir():
    if os.path.isfile('filmes_chacal.txt') == True:

        remover = str(input('Digite o nome do filme p/ excluir da lista.: '))
        arquivo = open('filmes_chacal.txt', 'r')

        for itens in arquivo:

            if itens == remover:
                print('É Igual')
            else:
                print('É Diferente')

        arquivo.close()
        #print('Filme excluido com sucesso!')

main()

#
