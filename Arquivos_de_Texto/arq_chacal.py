#!/usr/bin/python3
# -*- coding: utf-8 -*-


# Abrindo arquivo
# (r)-Leitura / (w)-Escrita
# (x)-Execução - Criar arquivo
# Senão especificar, o modo (r) sera usado
arquivo = open('lista_chacal.txt', 'w')

# Escrevendo no arquivo
conteudo = '0'
while conteudo != 'fim':
    conteudo = input('Digite o nome de um filme ou serie.: ')
    if conteudo == 'fim':
        break
    arquivo.write(conteudo)
    arquivo.write('\n')

# Fechando arquivo p/ salvar
arquivo.close()


# Abrindo arquivo modo leitura
arquivo = open('lista_chacal.txt', 'r')

# Lendo o conteudo de um arquivo
# função read() = EX.: arquivo.read()
print(arquivo.read())
