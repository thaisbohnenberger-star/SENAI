conta = float(input("Digite o valor total da conta: "))

valor1 = conta // 3
felipe = conta - (2* valor1)

print("Carlos paga: R$", valor1)
print("André paga: R$", valor1)
print("Felipe paga: R$", felipe)
#Três amigos, Carlos, André e Felipe. decidiram rachar igualmente a conta de um bar. Faça um algoritmo 
# para ler o valor total da conta e imprimir quanto cada um deve pagar, mas faça com que Carlos e 
# André não paguem centavos. Ex: uma conta de R$101,53 resulta em R$33,00 para Carlos, R$33,00 para 
# André e R$35,53 para Felipe. 