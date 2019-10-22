#!/usr/bin/python
# -*- coding: utf-8 -*-

# Lista de valores
soma = []

# Variavel p/ setar verdadeiro ou falso no while
iniciar = True

while iniciar == True:
    try:
        num = int(input('\nDigite um valor ou 0 para finalizar.: '))

        if type(num) is int and num != 0:
            soma.append(num)
            print('\nLista de valores:',soma)
            print('Total.:',sum(soma))

        else:
            print('Total.:',sum(soma))
            print('Fim da operação')
            iniciar = False

    except ValueError:
        print('\nValor incorreto!')
        print('Digite apenas valores inteiros')
        print('Ou digite zero 0 p/ finalizar a operação\n')
