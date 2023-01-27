
class Conta:
    def __init__(self, numero, titular, saldo):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
    def deposita(self, valor):
        self.saldo += valor
    def saca(self, valor):
       if (self.saldo < valor):
        return False
       else:
            self.saldo -= valor
            return True

    def __str__(self):
        return "Dados da Conta: \nNumero: {} \nTitular: {} \nSaldo: {}".format(self.numero, self.titular,self.saldo)
    def transfere_para(self, destino, valor):
        retirou = self.saca(valor)
        if (retirou == False):
            return False
        else:
            destino.deposita(valor)
            return True
    def atualiza(self, taxa):
        self.saldo += self.saldo * taxa
        return self.saldo
    #if __name__ == '__main__':
