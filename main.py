from cliente import Cliente
from conta import Conta

cliente1 = Cliente('Júlio','156389927-23',29)
conta1 = Conta(cliente1,100.56, 70000)

select = input('\nSelecione uma opão abaixo:\nSacar = 1\nDepositar = 2\nConsultar Saldo = 3\n')
if select == '1':
    saque = int(input('Digite o valor do saque:'))
    total = conta1.sacar(saque)
elif select =='2':
    deposito = int(input('Digite o valor do deposito:'))
    total = conta1.depositar(deposito)
elif select == '3':
    conta1.consultarSaldo()



