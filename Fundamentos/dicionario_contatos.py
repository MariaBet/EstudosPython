#!/usr/bin/python
# -*- coding: utf-8 -*-

# Lista de contatos

# Criado discionario vazio
contatos = {}

# Fazendo input no dicionario, indicando chave e valor.
chave = input("Digite um nome para dicionario: ")
valor = input("Digite um numero de telefone para o dicionario: ")


while valor != '0':
    # Adicionando valores no dicionario
    # O metodo append() que é usado em lista não funciona em dicionarios
    # A sintaxe para adicionar um valor em dicionario é diferente, veja
    # abaixo ... dicionario[chave] = valor
    contatos[chave] = valor

    # Imprimindo dicionario contatos
    print(contatos)

    chave = input("Digite uma chave para dicionario: ")
    valor = input("Digite um valor para a chave do dicionaio: ")

print(contatos)
print("Se encontram na Agenda agora")

# Operadores in e not in
