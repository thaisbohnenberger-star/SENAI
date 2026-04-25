hora_normal = float(input("Escreva suas horas normais trabalhadas: "))
hora_extra = float(input("Escreva suas horas extra trabalhadas: "))

normal = hora_normal * 10
extra = hora_extra * 15

bruto = normal + extra
liquido = bruto - (bruto * 0.10)

print("Seu salário bruto deu: R$",bruto)
print("Seu salário final deu: R$",liquido)

#A empresa Hipotheticus paga R$10,00 por hora normal trabalhada, e R$15,00 por hora extra. Faça um 
#algoritmo para calcular e imprimir o salário bruto e o salário líquido de um determinado funcionário. 
#Considere que o salário líquido é igual ao salário bruto descontando-se 10% de impostos.