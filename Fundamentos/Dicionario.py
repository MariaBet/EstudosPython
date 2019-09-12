#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
Dicionário
Um dicionário é  mutável e indexada.
No Python, os dicionários são escritos com colchetes e possuem valores.
"""

Floresta = input("Digite no dicionario: ")
print("Sim, se encontra na floresta")
Floresta = {
    "Arvore": "Ipe",
    "Felino": "onca",
    "Madeira": "Sucupira",
    "Aves": "Sabia",
    "Lepidopera": "Borboleta"
}
Floresta["Pequi"] = "Brasilense"
for x in Floresta.values():  # imprimi cada nome da lista
    print(x)
