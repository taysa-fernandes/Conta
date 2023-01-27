from Conta import Conta
from ContaPoupanca import ContaPoupanca
from ContaCorrente import ContaCorrente
from AtualizadorContas import AtualizadorDeContas
c = Conta('123-4', 'Joao', 1000.0)
cc = ContaCorrente('123-5', 'Jose', 1000.0)
cp = ContaPoupanca('123-6', 'Maria', 1000.0)

c.atualiza(0.01)
cc.atualiza(0.01)
cp.atualiza(0.01)

print(c.saldo)
print(cc.saldo)
print(cp.saldo)
print(cc)
adc = AtualizadorDeContas(0.01)

adc.roda(c)
adc.roda(cc)
adc.roda(cp)
print('Saldo total: {}'.format(adc._saldo_total))