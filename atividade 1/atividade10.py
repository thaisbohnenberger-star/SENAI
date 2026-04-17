dias = int(input("Digite a quantidade de dias: "))

anos = dias // 360
resto = dias % 360

meses = resto // 30
dias_restantes = resto % 30

print("Tempo sem acidentes:")
print(anos, "ano(s)")
print(meses, "mês(es)")
print(dias_restantes, "dia(s)")