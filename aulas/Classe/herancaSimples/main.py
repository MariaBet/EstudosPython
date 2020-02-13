from classes import *

"""
Associação -Usa |Agregação - Tem | Composição- É dono | Herança - É
"""
c1 = Cliente('Luiz', 38)
c1.falar()
c1.comprar()

a1 = Aluno('Maria', 54)
a1.falar()
a1.estudar()

# estânciar
p1 = Pessoa('Gabriel', 65)
p1.falar()

print()

c2 = ClienteVIP('Rosinha', 28)
c2.falar()
