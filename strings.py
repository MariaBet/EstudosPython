#!/usr/bin/python
# -*- coding: utf-8 -*-
# strings são sequencias de caracteres com aspas("") ou ('')

fruta = "morango"
tipo = "sorvete de "
print( tipo + fruta )

# operacao com string
s = "python"
excl = "!"
print(s+excl*3)

# metodos de strings

ss = "Estudos, Python"
print(ss.upper())     # maiusculo
tt = ss.lower()       # minusculo
print(tt)
nn = ss.capitalize()   # primeira letra maiusculo
print(nn)

# comprimento da palavra
carro = "Mustang"
print(len(carro))

# comparacao

ford = "mustang"
if ford == "mustang":
    print("sim, Eu tenho um mustang!")
else:
    print("Nao, nao tenho um mustang!")
