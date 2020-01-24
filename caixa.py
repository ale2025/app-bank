from classes import Cliente, Conta

#funções do caixa eletronico

class CaixaEletronico():
  def __init__(self):
    nome = input('Qual è seu nome')
    cpf = input('Qual numero do cpf')

    cliente_banco = Cliente(nome, cpf)
    self.conta = Conta(cliente_banco)
    print(f'Olá, {self.conta.cliente.nome}, sua conta é {self.conta.numero_conta}')

  def exibir_menu(self):
    escolha = input('O que voce deseja fazer?\n1-Olhar o saldo\n2-Fazer depósito\n3-Fazer Saque')

    if escolha == "1":
      valor_saldo = self.conta.consultar_saldo()
      print(f'O seu saldo é {valor_saldo}')

    if escolha == "2":
      valor = float(input('Quanto você deseja depositar?'))
      self.conta.depositar(valor)
      print(f'Deu certo o seu depósito de {valor}.')

    if escolha == "3":
      valor = float(input('Quanto você deseja sacar?'))
      if valor > self.conta._saldo:
        print('Seu saldo é insuficiente.')
      elif valor > 0 and valor < self.conta._saldo:
        self.conta.sacar(valor)
        print('Seu saque deu certo.')