#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""Funções simples"""
def soma(n1, n2):
    return n1+n2

def subtracao(n1, n2):
    return n1-n2

"""Funções lambda"""
lab_soma = lambda num1,num2 : num1+num2
lab_subtracao = lambda num1,num2 : num1-num2


"""Chamando as funções"""
print('Resultados funções simples')
print('Soma.: ', soma(2,2))
print('Subtração.: ', subtracao(3,2),'\n')

print('Resultados funções lambda')
print('Soma.:',lab_soma(5,5))
print('Subtração.:',lab_subtracao(20,5),'\n')

# Lambda, nem sempre é possivel reduzir uma função para apenas uma linha
# Se nesta função você tiver alguns loops e condições! Fica inviavel

# Em python, conseguimos chamar uma função dentro de outra função kkkk
# vai vendo que sinistro rsrs.

# Por exemplo, se vc tem uma função comum que usa a formula de equação do
# 2º grau. Onde vc tem mais de uma operação na formula. Algo assim que eu
# entendi rsrs.


"""Função lambda chamando outra função comum"""
# Chamando função dentro de outra função
# Exemplo usando uma expressão simples
# 23+50-2*5
lamb_exp = lambda: subtracao(soma(23,50),(2*5))
print('O resultado da expressão 23+50-2*5 é.:',lamb_exp())
