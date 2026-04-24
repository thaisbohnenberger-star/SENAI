conta = float(input("Digite o valor total da conta: "))

parte = conta / 3

carlos = int(parte)
andre = int(parte)

felipe = round(conta - carlos - andre, 2)

print("Carlos paga: R$", carlos)
print("André paga: R$", andre)
print("Felipe paga: R$", felipe)