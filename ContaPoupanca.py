from Conta import Conta
from Historico import Historico
class ContaPoupanca(Conta):
    def __init__(self, numero, titular, saldo):
        super().__init__(numero, titular, saldo)
    def atualiza(self, taxa):
        self.saldo += self.saldo * taxa * 3
        return self.saldo