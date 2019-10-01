#!/usr/bin/python3
# -*- coding: utf-8 -*-

# importando modulos simples
import math

# verificando os modulos importados
print('Modulos importados de forma geral.: ',dir(),'\n')

# verificando funções do modulo importado
# neste caso, o modulo math
print('O que tem no modulo math importado.: ',dir(math),'\n')

# Calculando a raiz quadrada de um valor
num = int(input('Digite um numero.: '))
print('A raiz quadrada de',num,'é.:',math.sqrt(num),'\n')

# Importando todas as funções do modulo funcao_calc
from funcao_calc import *
