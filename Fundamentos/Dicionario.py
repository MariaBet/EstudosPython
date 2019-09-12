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
Floresta ["Pequi"] = "Brasilense"
for x in Floresta.values():  # imprimi cada nome da lista
    print(x)



# Fazendo input no dicionario, indicando chave e valor.
chave = input("Digite uma chave para dicionario: ")
valor = input("Digite um valor para a chave do dicionaio: ")

# Adicionando valores no dicionario
# O metodo append() que é usado em lista não funciona em dicionarios
# A sintaxe para adicionar um valor em dicionario é diferente, veja
# abaixo ... dicionario[chave] = valor
Floresta[chave] = valor

# Imprimindo dicionario contatos
print(Floresta)
