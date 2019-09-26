#!/usr/bin/python3
# -*- coding: utf-8 -*-

n1 = int(input("Digite um valor: "))
n2 = int(input("Digite um valor: "))
n3 = int(input("Digite um valor: "))
#valores_expres = lambda n1, n2, n3 : (n1 + n2), ( n2 * n3)
valores_expres = lambda: ((n1+n2)-(n2*n3))
print('O valor da expressão é: ', valores_expres())
