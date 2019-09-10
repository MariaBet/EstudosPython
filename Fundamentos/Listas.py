#!/usr/bin/python
# -*- coding: utf-8 -*-

# Listas
carros=['ferrari','uno','gol','palio','jeep','troller']

carros.sort()  # classifica a lista crescente por padrao
print (carros)
carros[0]='bugati'; #nao está na lista acima, mas aqui voce adiciona

for item in carros:           # lacos
    print (item.capitalize())   # capitalize caixa alta






# listas de convidados exemplo adicionar depois


convidados = []       # lista vazia
convidados.append('Monique')
convidados.append('Eduardo ')
convidados.append('Chacal')
convidados.append('Betania')
convidados.append('Cristiano')
print("Tenho ", len(convidados), "Convidados")   # a quantidade de convidados
convidados.sort()      # ordem alfabetica
print("Sao esses: ")
print(convidados)
print("O primeiro convidado", convidados[0])
for convidado in convidados:   # ira repetir 5 vezes
    print("Os convidados terao que vim a carater de gala")
