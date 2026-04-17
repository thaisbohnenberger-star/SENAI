salario = int(input("Escreva seu salário bruto: "))

aumento = salario + (salario * (15 / 100))
imposto = aumento - (aumento * (8 / 100))

print("Seu salário final deu: R$",imposto)