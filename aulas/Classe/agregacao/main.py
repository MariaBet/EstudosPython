from classes import CarrinhoDeCompras, Produto


carrinho = CarrinhoDeCompras()

p1 = Produto('Arroz', 10)
p2 = Produto('Feijão', 20)
p3 = Produto('Panela', 60)


carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)
carrinho.inserir_produto(p3)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p1)
carrinho.inserir_produto(p3)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)

carrinho.lista_produto()
print(carrinho.soma_total())
