#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Os operadores logicos são usados para combinar condiocionais
and, or not
os operadores aritimeticos são usados com valores numericos
+ - * / % ** //
mais, menos, multiplicacao, divisao, modulo, exponenciacao, e resto da divisao
Os operadores de atribuicao usados para atribuir valores a variaveis
= igual
+= mais e igual
Os operadores de associacao- testa a sequencia apresentada
in e not in
"""
# operadores logicos
n = 10
print(n < 5 and n > 8)

m = 12
print(m < 6 or m > 9)

t = 20
print(not(t > 22 and t < 24))  # retorna true -verificar

# operadores aritimeticos

E = 33
B = 28
print (E, B)

E = 33
B = 28
print(E * B)

# operadores de atribuicao
c = 33
print(c)

y = 9
y += 6
print(y)


# operadores de associacao
floresta = ("Cerrado", "Caatinga", "Campo")
print("Cerrado" in floresta)   # retorna true
