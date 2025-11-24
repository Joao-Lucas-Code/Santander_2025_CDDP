MAIOR_IDADE = 18
IDADE_ESPECIAL = 12

idade = int(input("Digite a sua idade: "))

if idade >= MAIOR_IDADE:
    print("Você é maior de idade, e pode tirar a CNH")

if idade < MAIOR_IDADE:
    print("Você é menor de idade, e não pode tirar a CNH")

if idade == IDADE_ESPECIAL:
    print("Você tem 12 anos, idade especial, pode fazer aulas teóricas da CNH")