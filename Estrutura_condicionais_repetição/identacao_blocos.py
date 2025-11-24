def sacar(valor):
  saldo = 500

  if saldo >= valor:
    saldo -= valor
    print("Saque realizado com sucesso!")
    print(f"Saldo restante: {saldo}")
  else:
    print("Saldo insuficiente para realizar o saque.")
    
def depoitar(valor):
  saldo = 500

  if valor > 0:
    saldo += valor
    print('Você depositou:', valor)
    print("Depósito realizado com sucesso!")
    print(f"Saldo atual: {saldo}")
  else:
    print("Valor de depósito inválido.")

sacar(600)
sacar(400)
print('---')
depoitar(200)
depoitar(-50)