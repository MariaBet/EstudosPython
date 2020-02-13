

"""
public, protected, private
Dentro e fora, dentro e filhas e somente dentro da classe
_protected
__privado
"""


class BaseDeDados:
    def __init__(self):
        self._dados = {}

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self._dados:
            self._dados['clientes'] = {id: nome}
        else:
            self._dados['clientes'].update({id: nome})

    def lista_clientes(self):
        for id, nome in self._dados['clientes'].items():
            print(id, nome)

    def apaga_clientes(self, id):
        del self._dados['clientes'][id]

bd = BaseDeDados()
bd.inserir_cliente(1, 'Maria')
bd.inserir_cliente(2, 'Eduardo')
bd.inserir_cliente(3, 'Chacal')
# bd.dados = "Um outro programa" aqui quebra a classe
bd.lista_clientes()

# __PRIVATE


class BaseDeDados:
    def __init__(self):
        self.__dados = {}

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)

    def apaga_clientes(self, id):
        del self.__dados['clientes'][id]

bd = BaseDeDados()
bd.inserir_cliente(1, 'Maria')
bd.inserir_cliente(2, 'Eduardo')
bd.inserir_cliente(3, 'Chacal')
bd.__dados = "Um outro programa"  # aqui quebra a classe
# bd.lista_clientes()
# print(bd.__dados)
print(bd._BaseDeDados__dados)
