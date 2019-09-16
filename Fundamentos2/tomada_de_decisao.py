#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Os operadores de tomada de decisao
"""
# If, Elif, Else
# usando o exemplo de indentacao.py idade.


idade = int(input("Qual a sua idade?: "))
if idade == 30:
    print("Voce tem 30 anos, foi aceito, boa sorte")
elif idade < 30:
    print("Voce nao esta apto a participar: ")
else:
    print("Voce tem mais de 30 anos, voce foi aceito, boa sorte")
