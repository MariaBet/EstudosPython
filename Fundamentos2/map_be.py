#!/usr/bin/python3
# -*- coding: utf-8 -*-
from functools import reduce


soma = reduce((lambda x, y: x + y), [1, 2, 3, 4])
print(soma, '\n')

# reduce() outra função nativa do python, ela vai aplicar uma função em todos
# os valores passados em forma de lista, e retornar apenas um valor.
"""
Curiosidade: reduce faz parte da lib functools, ou seja, precisamos
importar esta biblioteca antes de utilizá-la.
A função foi ‘dropada’ do core quando Python passou para a versão 3.
Vamos observar como podemos utilizar reduce():
"""

# map() serve para aplicarmos uma função a cada um dos elementos passado
# em lista como argumento a ela.

itens = [1, 2, 3, 4, 5, 6, 7, 8]
dobro = list(map(lambda x: x * 2, itens,))
print(dobro, '\n')

# Com o nome autoexplicativo, a função filter() filtra os elementos passados
# na função, de acordo com a função passada como primeiro argumento.


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100, 99, 88, 66, 56, 78, 12, 4, 2, 3]
pares = list(filter(lambda x: x % 2 == 0, lista))
print(pares, '\n')































# retirado daqui https://medium.com/horadecodar/express%C3%B5es-
# lambda-em-python-com-map-reduce-e-filter-a391368ae886
