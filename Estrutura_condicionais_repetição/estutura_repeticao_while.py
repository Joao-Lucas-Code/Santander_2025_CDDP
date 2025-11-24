opcao = -1

while opcao != 0:
  opcao = int(input("[1] Sacar\n[2] Depositar\n[0] Sair\nEscolha uma opção: "))

  if opcao == 1:
    valor_saque = float(input("Digite o valor para saque: "))
    print(f"Saque de R${valor_saque} realizado com sucesso!")
  elif opcao == 2:
    valor_deposito = float(input("Digite o valor para depósito: "))
    print(f"Depósito de R${valor_deposito} realizado com sucesso!")
  elif opcao == 0:
    print("Saindo do sistema. Obrigado por usar nosso banco!")
  else:
    print("Opção inválida. Por favor, tente novamente.")