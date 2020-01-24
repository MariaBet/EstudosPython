#!/usr/bin/python3
# -*- coding: utf-8 -*-

roupa = 'o rato roeu a roupa do rei de roma.'
tamanho_string = len(roupa)
c = 0
nova_roupa = ''
while c < tamanho_string :

    if roupa[c] == 'r':
        nova_roupa = nova_roupa + roupa[c].upper()
    else:
        nova_roupa = nova_roupa + roupa[c]
    print(nova_roupa)


    c += 1
# print(nova_roupa)
