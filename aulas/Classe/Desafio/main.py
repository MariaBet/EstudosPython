from banco.banco import Banco
from banco.contacorrente import ContaCorrente
from banco.contapoupanca import ContaPoupanca
from pessoas.cliente import Cliente

banco = Banco()

cliente1 = Cliente('Luiz', 25)
cliente2 = Cliente('Maria', 52)
conta1 = ContaPoupanca(1111, 32460, 0)
conta2 = ContaCorrente(2222, 32461, 0)
cliente1.inserir_conta(conta1)
cliente2.inserir_conta(conta2)

banco.inserir_conta(conta1)
banco.inserir_cliente(cliente1)
banco.inserir_conta(conta2)
banco.inserir_cliente(cliente2)

if banco.autenticar(cliente1):
    cliente1.conta.depositar(1000)
    cliente1.conta.sacar(10)
else:
    print('Cliente não autenticado.')

print('###############################')

if banco.autenticar(cliente2):
    cliente2.conta.depositar(1000)
    cliente2.conta.sacar(10)
else:
    print('Cliente não autenticado.')

