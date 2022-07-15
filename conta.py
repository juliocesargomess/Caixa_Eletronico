class Conta():

    def __init__(self, cliente, saldo, limite):
        self.cliente = cliente
        self.saldo = saldo
        self.limite = limite

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            if self.saldo > self.limite:
                self.saldo = self.limite

        else:
            print("valor inválido")
        print("Seu saldo atualizado é: ", self.saldo)

    def sacar(self, valor):
        if valor <= self.saldo and valor > 0:
            self.saldo -= valor
            print("seu saque é de:", valor,"\nO total em conta é:", self.saldo)
        else:
            print("Valor de Saque inválido")

    def consultarSaldo(self):
        return print("Seu saldo é:", self.saldo)