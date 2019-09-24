#!/usr/bin/python3
# -*- coding: utf-8 -*-


def minha_floresta(Arvores, Passaros):
    print(Arvores)
    print(Passaros)


minha_floresta("Arvores", "Sucupira, Ipe, Figueira, Jaca, Caju")
minha_floresta("Passaros", "Sabia, Tico-Tico, Canario, Tucano, Papagaio " '\n')


def print_somente(nome, idade):
    print("Meu nome eh: ", nome, "Minha idade eh: ", idade, '\n')


print_somente("Eduardo" '\n', 33)


def print_convocados(*membros):
    for convocados in membros:
        print("Esse membro está na comunidade: ", convocados)


print_convocados("Monique", "Maria Betania", "Eduardo", "Eduardo Campacci")
