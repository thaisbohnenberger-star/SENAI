import time
temperatura = 20

while temperatura <= 38:
    print(f"Aquecendo... Temperatura atual: {temperatura}°C")
    temperatura += 1
    time.sleep(1)

#Grupo 8: Controle de Climatização (Aquecedor)
#Problema: Iniciar em 20°C e chegar a 38°C.
#Detalhes: Aumentar de 1 em 1 grau. Para cada grau, exibir: "Aquecendo... Temperatura atual: [X]°C".
#Objetivo Técnico: Laço simples de contagem progressiva.
#Variáveis: temperatura.