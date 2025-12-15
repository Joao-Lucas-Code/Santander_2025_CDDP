N = int(input())

totais = {
    "saco": 0.0,
    "papelao ondulado": 0.0,
    "papel kraft": 0.0
}

for _ in range(N):
    linha = input()
    
    partes = [parte.strip() for parte in linha.split(',')]
    
    if len(partes) == 3:
        embalagem = partes[1]
        quantidade_str = partes[2]
        
        quantidade = float(quantidade_str)

        if embalagem in totais:
            totais[embalagem] += quantidade

for tipo in ["saco", "papelao ondulado", "papel kraft"]:
    total_toneladas = totais[tipo]
    
    if total_toneladas == int(total_toneladas):
        print(f"{tipo}: {int(total_toneladas)}")
    else:
        print(f"{tipo}: {total_toneladas}")