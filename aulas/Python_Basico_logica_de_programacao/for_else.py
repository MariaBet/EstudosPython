

nomes = ("João", "Eduardo", "Maria", "Betania", "Augusta")

for valor in nomes:
    if valor.startswith('J'):
        print("Começa com 'J'", valor)
    else:
        print("Não começa com 'J'", valor)

print()

comeca_j = False
for valor in nomes:
    if valor.startswith('J'):
        comeca_j = True
if comeca_j:
    print("Existe um nome que começa com 'J'")
else:
    print("Não existe um nome que começa com 'J'")
