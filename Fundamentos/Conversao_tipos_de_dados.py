#!/usr/bin/python
# -*- coding: utf-8 -*-


# A conversao de dados serve p/ que seja possivel pegar um dado de um tipo
# e gerar qualquer tipo de saida do dado em questao

# Entao apenas a saida é convertida, mas o tipo da variavel permanece
# Para converter a variavel em sí, devemos fazer com que a variavel
# receba ela mesma com saida convertidaself.

# Exemplo:

# variavel = "10"
# variavel = int(variavel)

# Variaveis
inteiro = 10
flutuante = 3.5
texto = "2019"


# Conversao int p/ float
print(float(inteiro))

# Conversao float p/ int
print(int(flutuante))

# Conversao int p/ string
print(str(inteiro))

# Conversao string p/ int
print(int(texto))

# Sinal de + concatena duas informações
print(texto + str(10))

# Sinal de + soma dois números
print(inteiro + 10)
