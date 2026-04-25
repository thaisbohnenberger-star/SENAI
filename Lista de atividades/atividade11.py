dias = int(input("Digite a quantidade de dias: "))

anos = dias // 360
resto = dias % 360

meses = resto // 30
dias_restantes = resto % 30

print("Tempo sem acidentes:")
print(anos, "ano(s)")
print(meses, "mês(es)")
print(dias_restantes, "dia(s)")
#Uma fábrica controla o tempo de trabalho sem acidentes pela quantidade de dias. Faça um algoritmo 
# para converter este tempo em anos, meses e dias. Assuma que cada mês possui sempre 30 dias. 