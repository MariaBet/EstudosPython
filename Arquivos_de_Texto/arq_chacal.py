#!/usr/bin/python3
# -*- coding: utf-8 -*-


# Abrindo arquivo
# (r)-Leitura / (w)-Escrita
# (x)-Execução - Criar arquivo
# Senão especificar, o modo (r) sera usado
arquivo = open('lista_chacal.txt', 'w')

# Escrevendo no arquivo
arquivo.write(input('Digite o nome do filme ou serie.: '))


# Fechando arquivo p/ salvar
arquivo.close()



# Abrindo arquivo modo leitura
arquivo = open('lista_chacal.txt', 'r')

# Lendo o conteudo de um arquivo
# função read() = EX.: arquivo.read()
print(arquivo.read())
