'''meus exemplos'''


class Conta:
    def __init__(self,numconta, cliente, limite, saldo=0):
        self.numconta=numconta
        self.cliente=cliente
        self.saldo=saldo
        self.limite=limite


        print(f'Conta:{self.numconta} -- Cliente:{self.cliente} -- Saldo:{self.saldo} -- Cheque especial:{self.limite}')

    def depositar(self,deposito):
        if deposito>0:
            self.saldo+=deposito
            print(f'Depósito de R$ {deposito} realizado com sucesso! Novo saldo: R$ {self.saldo}')
            o = input('Realizar alguma operação [s/n]: ')
            inicio(o)


    def sacar(self,saque):
        if self.saldo+self.limite>=saque:
            self.saldo=(self.saldo+self.limite-saque)-self.limite
            print(f'Saque no valor de R$ {saque} foi realizado com sucesso! Novo saldo: R$ {self.saldo}')
            o = input('Realizar operação [s/n]: ')
            inicio(o)
        else:
            print(f'Seu saldo é insuficiente: {self.saldo}')
            o = input('Realizar operação [s/n]: ')
            inicio(o)

    def calcularRendimento(self):
        rend=self.saldo+self.saldo*(10/100)
        print(f'Rendimento foi {self.saldo*10/100}. Novo saldo: {rend}')
        o = input('Realizar operação [s/n]: ')
        inicio(o)

conta1=Conta(784,'Marta',100,450)
conta2=Conta(874,'Joao',200, 1320)
conta3=Conta(458,'Pedro',150,700)

contas=[conta1,conta2,conta3]

def operacoes():
    opcao=int(input('------ SELECIONE A CONTA ------:\n'
                            'Digite o número da conta: '))
    for i in contas:
        if opcao==i.numconta:
            operacao=input('Deseja Depositar [d] ou Sacar [s] ou Ver Rendimentos [r]: ')
            if operacao in 'dD':
                deposito=float(input('Digite o valor do Depósito: '))
                i.depositar(deposito)

            if operacao in 'sS':
                saque=float(input('Digite o valor do saque: '))
                i.sacar(saque)

            if operacao in 'rR':
                i.calcularRendimento()



def inicio(opcao):
    if opcao in 'sS':
        operacoes()
    else:
        print('Você Saiu! Volte sempre!')

opcao1 = input('Realizar operação [s/n]: ')
inicio(opcao1)















