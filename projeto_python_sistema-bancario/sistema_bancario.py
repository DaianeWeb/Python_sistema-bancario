class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print("Depósito de", valor, "realizado com sucesso.")
        else:
            print("Valor inválido para depósito.")

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print("Saque de", valor, "realizado com sucesso.")
        else:
            print("Saldo insuficiente ou valor inválido para saque.")

    def verificar_saldo(self):
        print("Saldo disponível:", self.saldo)


# Função para interagir com o sistema
def main():
    print("Bem-vindo ao Banco XYZ!")
    nome = input("Por favor, digite seu nome: ")
    conta = ContaBancaria(nome)

    while True:
        print("\Menu:")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Verificar Saldo")
        print("4. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            valor = float(input("Digite o valor a ser depositado: "))
            conta.depositar(valor)
        elif escolha == '2':
            valor = float(input("Digite o valor a ser sacado: "))
            conta.sacar(valor)
        elif escolha == '3':
            conta.verificar_saldo()
        elif escolha == '4':
            print("Obrigado por utilizar nossos serviços. Volte sempre!")
            break
        else:
            print("Opção inválida. Por favor, escolha novamente.")


if __name__ == "__main__":
    main()
