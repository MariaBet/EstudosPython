#!/usr/bin/python
# -*- coding: utf-8 -*-

# Criado uma lista de nomes.
nomes = ["Eduardo", "Betania", "Lia", "Maria"];

# Imprimindo a lista de acordo com a posição dos indices
print(nomes[0])   # 'Eduardo'
print(nomes[1])   # 'Betania'
print(nomes[2])   # 'Lia'
print(nomes[3])   # 'Maria'

# Lista com diversos tipos de informações
diversos = ["Chacal", 10, 3.2, "Betania"]
print(diversos[0])
print(diversos[1])
print(diversos[2])
print(diversos[3])

# Percorrendo uma lista de forma mais simples e elegante rsrs
linux = ['redhat', 'centos', 'debian', 'fedora', 'opensuse', 'arch']
for distro in linux:
    print (distro)

# Juntando todas as listas criadas ate aqui
fusao = nomes + diversos + linux
print (fusao)




# TRABALHANDO COM FUNCOES NATIVAS DE LISTAS

# Criando uma lista vazia
animais = [];

# Append - Adiciona o elemento no final da lista
animais.append("Leao") # Nao funcionou o acento rsrs
animais.append("Touro")
animais.append("Pinguim")
print(animais)

# Index - Retorna o index dos elementos
print(animais.index("Leao")) # 0

# Insert - Adiciona elemento em determinada posicao do Index
# Caso a posição ja tenha valor, ele nao exclui ... ele adiciona
# o elemento na posicao desejada e empurra o valor atual para frente
animais.insert(2, "gato")
print(animais)

# Remove - Remove pelo valor
animais.remove("gato")
print(animais)

# Pop - Remove pelo indice
animais.pop(2)
print(animais)

# Sort - Ordenar uma lista
print(fusao)
fusao.sort()
print(fusao)
