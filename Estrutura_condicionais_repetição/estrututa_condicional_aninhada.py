conta_normal = False
conta_universitaria = True

saldo = 2000
saque = 2000
cheque_especial = 500

if conta_normal:
    if saldo >= saque:
        saldo -= saque
        print("Saque realizado com sucesso!")
        print(f"Saldo restante: {saldo}")
    else:
        if saque <= (saldo + cheque_especial):
            saldo -= saque
            print("Saque realizado com uso do cheque especial!")
            print(f"Saldo restante: {saldo}")
        else:
            print("Saldo insuficiente para realizar o saque.")
elif conta_universitaria:
    if saque <= 500:
        if saldo >= saque:
            saldo -= saque
            print("Saque realizado com sucesso!")
            print(f"Saldo restante: {saldo}")
        else:
            print("Saldo insuficiente para realizar o saque.")
    else:
        print("Limite de saque para conta universitária é de R$500.")