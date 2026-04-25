salario = int(input("Escreva seu salário bruto: "))

aumento = salario + (salario * (15 / 100))
imposto = aumento - (aumento * (8 / 100))

print("Seu salário final deu: R$",imposto)
#Faça um algoritmo para ler o salário de um funcionário e aumentá-Io em 15%. Após o aumento, 
# desconte 8% de impostos. Imprima o salário inicial, o salário com o aumento e o salário final. 