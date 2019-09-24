#!/usr/bin/python3
# -*- coding: utf-8 -*-


def minha_floresta(Arvores, Passaros):
    print(Arvores)
    print(Passaros)


minha_floresta("Arvores", "Sucupira, Ipe, Figueira, Jaca, Caju")
minha_floresta("Passaros", "Sabia, Tico-Tico, Canario, Tucano, Papagaio " '\n')


def print_somente(nome, idade):
    print("Meu nome eh: ", nome, "Minha idade eh: ", idade, '\n')


print_somente("Eduardo" '\n', 33, sep='')


def print_lista(*membros):
    for lista in membros:
        print("Esse membro está na comunidade: ", lista)


print_lista("Monique", "Maria Betania", "Eduardo Barbosa", "Eduardo Campacci")
