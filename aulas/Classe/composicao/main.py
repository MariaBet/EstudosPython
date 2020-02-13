from classes import Cliente

Cliente1 = Cliente('Maria', 36)
Cliente1.insere_endereco('Belo Horizonte', 'MG')
print(Cliente1.nome)
Cliente1.lista_enderecos()
del Cliente1
print()

Cliente2 = Cliente('Rodrigo', 38)
Cliente2.insere_endereco('Salvador', 'BA')
Cliente2.insere_endereco('Gramado', 'RS')
print(Cliente2.nome)
Cliente2.lista_enderecos()
del Cliente2
print()

Cliente3 = Cliente('Cristiano', 49)
Cliente3.insere_endereco('Espirito Santo', 'ES')
print(Cliente3.nome)
Cliente3.lista_enderecos()
del Cliente3
print()

print('####################################################################')
