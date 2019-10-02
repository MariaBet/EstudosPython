#!/usr/bin/python3
# -*- coding: utf-8 -*-
<<<<<<< HEAD
=======

# Abrindo arquivo
# (r)-Leitura / (w)-Escrita
# (x)-Execução - Criar arquivo
# Senão especificar, o modo (r) sera usado
arquivo = open('lista_chacal.txt', 'r')

# Escrevendo no arquivo
arquivo.write(input('Digite o nome do filme ou serie.: '))


# Fechando arquivo p/ salvar
arquivo.close()



# Abrindo arquivo modo leitura
arquivo = open('lista_chacal.txt', 'r')

# Lendo o conteudo de um arquivo
# função read() = EX.: arquivo.read()
print(arquivo.read())
>>>>>>> 8fe6e93b88f38acc384c03a64a6a88830f0bba58
