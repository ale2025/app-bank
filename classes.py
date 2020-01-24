from random import randint


class Cliente():
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.pais = "Brasil"

class Conta():
    def __init__(self, cliente):
        self.cliente = cliente
        self.numero_conta = self._gerar()    
        self._saldo = 0

    def extrato(self):
        print(f'Numero: {self.conta}\nSaldo: {self._saldo}')

    def consultar_saldo(self):
        return self._saldo

    def depositar(self, valor_deposito):
        self._saldo += valor_deposito

    def sacar(self, valor_saque):
        self._saldo -= valor_saque

    def _gerar(self):
        self.random_numero = f'{randint(1000, 9999)}-{randint(1, 9)}'
        return self.random_numero
