# HANDS ON 2: MATRIZ APLICADA - MONITORAMENTO DE SENSORES
# 5 sensores, 24 medições por sensor (horas do dia)
# float sensores[5][24]

# 1. DECLARAÇÃO DA MATRIZ
sensores = []
print("MONITORAMENTO DE TEMPERATURA - 5 SENSORES x 24 HORAS")
print("\n ENTRADA DE DADOS ")

for i in range(5):
    print(f"\nSensor {i+1}:")
    linha_sensor = []
    for j in range(24):
        temperatura = float(input(f"  Hora {j}: "))
        linha_sensor.append(temperatura)
    sensores.append(linha_sensor)


maior_temp = sensores[0][0]
sensor_maior = 0
horario_maior = 0

soma_geral = 0
media_sensor = [0.0] * 5
acima_limite = 0

limite = float(input("\nDigite o valor limite para verificar leituras acima: "))


for i in range(5):  
    soma_sensor = 0
    for j in range(24):  
        temp = sensores[i][j]
        
        
        soma_geral += temp
        soma_sensor += temp
        
        
        if temp > maior_temp:
            maior_temp = temp
            sensor_maior = i
            horario_maior = j
        
       
        if temp > limite:
            acima_limite += 1
    
    
    media_sensor[i] = soma_sensor / 24


media_geral = soma_geral / (5 * 24)



medias_com_sensores = []
for i in range(5):
    medias_com_sensores.append((media_sensor[i], i + 1))

for i in range(1, len(medias_com_sensores)):
    chave_media, chave_sensor = medias_com_sensores[i]
    j = i - 1
    

    while j >= 0 and medias_com_sensores[j][0] > chave_media:
        medias_com_sensores[j + 1] = medias_com_sensores[j]
        j -= 1
    
    medias_com_sensores[j + 1] = (chave_media, chave_sensor)


print("\nRESULTADOS DO MONITORAMENTO")
print("\n1. MÉDIA DE CADA SENSOR:")
for i in range(5):
    print(f"   Sensor {i+1}: {media_sensor[i]:.2f} °C")

print(f"\n2. MAIOR TEMPERATURA REGISTRADA:")
print(f"   Valor: {maior_temp:.2f} °C")
print(f"   Sensor: {sensor_maior + 1}")
print(f"   Horário: {horario_maior}h")

print(f"\n3. MÉDIA GERAL (5 sensores × 24 horas):")
print(f"   {media_geral:.2f} °C")

print(f"\n4. LEITURAS ACIMA DO LIMITE ({limite} °C):")
print(f"   Quantidade: {acima_limite} medições")

print("\n5. SENSORES ORDENADOS POR MÉDIA (Insertion Sort):")
print("   (Do menor para o maior)")
for media, sensor in medias_com_sensores:
    print(f"   Sensor {sensor}: {media:.2f} °C")
