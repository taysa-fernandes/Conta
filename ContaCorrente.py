from Conta import Conta
from Historico import Historico
class ContaCorrente(Conta):
    def __init__(self,numero, titular, saldo):
        super().__init__(numero, titular, saldo)
    def atualiza(self, taxa):
        self.saldo += self.saldo * taxa * 2
        return self.saldo
    def deposita(self, valor):
        self.saldo += valor - 0.10