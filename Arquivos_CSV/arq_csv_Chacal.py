#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Importar modulo CSV
import pandas


# Carrega dados
arquivo = pandas.read_csv('dados.csv')

# Imprime informações
print(arquivo.head(5))
print(arquivo.tail(20))
