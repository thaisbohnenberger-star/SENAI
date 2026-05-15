import time
# Apresentação
print("Seja bem vindo(a) ao grupo 8, os alunos deste grupo são: Flávia, Julio e Thais!")

# Pedindo temperaturas ao usuário
temp_atual = int(input("\nDigite sua temperatura atual: "))
temp_desejada = int(input("Digite qual temperatura você deseja: "))

# Verificação
if temp_desejada <= temp_atual:
    print("Erro: a temperatura desejada deve ser maior que a atual.")
else:
    temperatura = temp_atual

    # Simulação de aquecimento
    while temperatura <= temp_desejada:
        if temperatura < 25:
            led = "AZUL 🔵 (Fria)"
        elif temperatura < 30:
            led = "AMARELO 🟡 (Morno)"
        elif temperatura <= 35:
            led = "VERDE 🟢 (Ideal)"
        else:
            led = "VERMELHO 🔴 (Quente)"
        print(f"Aquecendo... Temperatura atual: {temperatura}°C - LED: {led}")
        temperatura += 1
        time.sleep(2)
print("Temperatura ideal atingida. Aquecedor desligado")

#Grupo 8: Controle de Climatização (Aquecedor)
#Problema: Iniciar em 20°C e chegar a 38°C.
#Detalhes: Aumentar de 1 em 1 grau. Para cada grau, exibir: "Aquecendo... Temperatura atual: [X]°C".
#Objetivo Técnico: Laço simples de contagem progressiva.
#Variáveis: temperatura.