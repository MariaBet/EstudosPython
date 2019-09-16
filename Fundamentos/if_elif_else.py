#!/usr/bin/python3
# -*- coding: utf-8 -*-


prova = float(input('Digite a nota da prova.: '))
trabalho = float(input('Digite a nota da prova.: '))
nota = (prova + trabalho) / 2

# Tomada de decisao, o que entendi do elif é que ele substitui a utilização
# de IF's encadeados, portanto podemos usar diversos elif
if nota < 3.0:
    print("Reprovado")
elif nota < 5.0:
    print("Recuperacao")
elif nota < 9.0:
    print("Aprovado")
else:
    print("Aprovado com louvor!")

# Pulando uma linha
print('\n')
