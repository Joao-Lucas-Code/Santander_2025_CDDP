N = int(input())

totais = {}
paises_ordenados = []

for _ in range(N):
    linha = input()
    
    partes = [parte.strip() for parte in linha.split(',')]
    
    if len(partes) == 2:
        pais = partes[0]
        quantidade = float(partes[1])
    else:
        partes = linha.split()
        if len(partes) >= 2:
            quantidade = float(partes[-1])
            pais = " ".join(partes[:-1])
        else:
            continue

    if pais not in paises_ordenados:
        paises_ordenados.append(pais)
        totais[pais] = 0.0

    totais[pais] += quantidade

for pais in paises_ordenados:
    total_toneladas = totais[pais]
    
    if total_toneladas == int(total_toneladas):
        print(f"{pais}: {int(total_toneladas)} toneladas")
    else:
        print(f"{pais}: {total_toneladas} toneladas")