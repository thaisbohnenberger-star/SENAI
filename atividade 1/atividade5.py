dia = int(input("Digite o dia da entrega: "))
mes = int(input("Digite o mês da entrega: "))
if dia < 1 or dia > 30 or mes < 1 or mes > 12:
    print("Data inválida! Considere meses de 1 a 12 e dias de 1 a 30.")
else:
    total_dias = 0
    for i in range(1, mes):
        total_dias += 30
    total_dias += dia
    print(f"Total de dias decorridos desde o início do ano: {total_dias}")