# Atividade Avaliativa - 4
# Investigação do Array de Temperaturas

print("PROGRAMA DE ANÁLISE DE TEMPERATURAS")

temperaturas = []

print("\n ENTRADA DE DADOS")
for i in range(10):
    while True:
        try:
            valor = float(input(f"Digite a temperatura do índice {i}: "))
            temperaturas.append(valor)
            break
        except ValueError:
            print("Erro! Digite um número válido.")


print("\n TEMPERATURAS ARMAZENADAS ")
print("Índice | Temperatura")
for i in range(10):
    print(f"  {i:2d}   |   {temperaturas[i]:.1f}°C")


soma = 0
maior = temperaturas[0]
menor = temperaturas[0]
indice_maior = 0
indice_menor = 0


for i in range(10):
    
    soma += temperaturas[i]
    
   
    if temperaturas[i] > maior:
        maior = temperaturas[i]
        indice_maior = i
    
   
    if temperaturas[i] < menor:
        menor = temperaturas[i]
        indice_menor = i

media = soma / 10


acima_media = 0
for i in range(10):
    if temperaturas[i] > media:
        acima_media += 1

temperaturas_ordenadas = temperaturas.copy()


for i in range(1, len(temperaturas_ordenadas)):
    chave = temperaturas_ordenadas[i]
    j = i - 1
    
    
    while j >= 0 and temperaturas_ordenadas[j] > chave:
        temperaturas_ordenadas[j + 1] = temperaturas_ordenadas[j]
        j -= 1
    
    temperaturas_ordenadas[j + 1] = chave


print("\nRESULTADOS DA ANÁLISE")
print(f"\n Média das temperaturas: {media:.2f}°C")
print(f" Maior temperatura: {maior:.1f}°C (índice {indice_maior})")
print(f" Menor temperatura: {menor:.1f}°C (índice {indice_menor})")
print(f" Valores acima da média: {acima_media}")

print("\n TEMPERATURAS ORDENADAS (Insertion Sort):")
print("Índice | Temperatura")
for i in range(10):
    print(f"  {i:2d}   |   {temperaturas_ordenadas[i]:.1f}°C")


print("\n INFORMAÇÕES ADICIONAIS COM DADOS ORDENADOS:")
print(f" Temperatura mais baixa: {temperaturas_ordenadas[0]:.1f}°C")
print(f" Temperatura mais alta: {temperaturas_ordenadas[9]:.1f}°C")
print(f" Mediana: {(temperaturas_ordenadas[4] + temperaturas_ordenadas[5]) / 2:.1f}°C")
print(f" Amplitude térmica: {temperaturas_ordenadas[9] - temperaturas_ordenadas[0]:.1f}°C")
