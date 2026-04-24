distancia = 0
x1 = float(input("Digite sua coordenada x do primeiro ponto: "))
y1 = float(input("Digite sua coordenada x do segundo ponto: "))
x2 = float(input("Digite sua coordenada x do terceiro ponto: "))
y2 = float(input("Digite sua primeira coordenada x do quarto ponto: "))

diferenca_x = x2 - x1
diferenca_y = y2 - y1

distancia ((diferenca_x ** 2) + (diferenca_y ** 2)) ** 0.5

print("A distancia entre os pontos é: ", format(x1, x2, y1, y2, distancia))