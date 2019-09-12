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
for x in Floresta.values():
    print(x)       # imprimi cada nome da lista que corresponde ao x


chave = input("Digite uma categoria: ")
valor = input("Digite uma especie: ")

while chave != '0' or valor != '0':
    # Adicionando valores no dicionario
    # O metodo append() que é usado em lista não funciona em dicionarios
    # A sintaxe para adicionar um valor em dicionario é diferente, veja
    # abaixo ... dicionario[chave] = valor
    Floresta[chave] = valor

    # Imprimindo dicionario contatos
    print(Floresta)

    chave = input("Digite uma categoria: ")
    valor = input("Digite uma especie: ")

print(Floresta)

# Quantidade de itens no dicionario Floresta
len(Floresta)

# Deletando um item do dicionario com del()
excluir = input("Digite o nome de um elemento para excluir: ")
del(Floresta[excluir])
print(Floresta)
