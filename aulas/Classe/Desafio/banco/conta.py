from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia, conta, saldo):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        self.detalhes()

    def detalhes(self):
        print(f'Agência: {self.agencia}', end=" ")
        print(f'Conta: {self.conta}', end=" ")
        print(f'Saldo: {self.saldo}')

    @abstractmethod
    def sacar(self, valor): pass