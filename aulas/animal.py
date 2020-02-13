class Animal:
    def __init__(self, nome, idade, raca):
        self.nome = nome
        self.idade = idade
        self.raca = raca


print('CLASSE ANIMAL \n')

a1 = Animal('Cachorro', 7, 'Pastor Alemão')
print(a1.nome)
print(a1.idade)
print(a1.raca)

print('############################1')
a2 = Animal('Gato', 6, 'Siames')
print(a2.nome)
print(a2.idade)
print(a2.raca)

print('############################2')

a3 = Animal('Tamanduá', 3, 'Melete')
print(a3.nome)
print(a3.idade)
print(a3.raca)
