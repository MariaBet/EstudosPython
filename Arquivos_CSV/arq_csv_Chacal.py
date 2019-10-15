#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Importar modulo pandas
import pandas

# Carrega dados
arquivo = pandas.read_csv('dados.csv')

# Imprimindo as 5 primeiras linhas do arquivo
print(arquivo.head(5))

# Imprimindo as 20 ultimas linhas do arquivo
print(arquivo.tail(20))

print('\n \n')

# imprimindo uma determinada linha
print(arquivo.loc[100])
print('\n \n')

# imprimindo uma determinda linha e coluna
print(arquivo.loc[10,'Cargo'])
print('\n \n')

# imprimindo um conjunto em sequencia de linhas e coluna
print(arquivo.loc[0:19,'Cargo'])
print('\n \n')
