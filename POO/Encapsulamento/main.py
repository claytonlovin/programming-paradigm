
class Conta:
    def __init__(self, saldo=0, numero_agencia=''):
        self._saldo = saldo
        self.numero_agencia = numero_agencia
    
    def depositar(self, valor):
        self._saldo += valor
    
    def sacar(self, valor):
        self._saldo -= valor

    def get_saldo(self):
        return self._saldo


conta = Conta(1000, "1234-5")

conta.depositar(1000)
print(conta.numero_agencia)
print(conta.get_saldo())