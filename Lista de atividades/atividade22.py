# Entrada das quantidades de cada moeda
m01 = int(input("Quantidade de moedas de 1 centavo: "))
m05 = int(input("Quantidade de moedas de 5 centavos: "))
m10 = int(input("Quantidade de moedas de 10 centavos: "))
m25 = int(input("Quantidade de moedas de 25 centavos: "))
m50 = int(input("Quantidade de moedas de 50 centavos: "))
m1r = int(input("Quantidade de moedas de 1 real: "))

# Cálculo do valor total em reais
total = (m01 * 0.01) + (m05 * 0.05) + (m10 * 0.10) + (m25 * 0.25) + (m50 * 0.50) + (m1r * 1.00)

# Exibição do resultado
print(f"O valor total economizado é: R$ {total:.2f}")

#Pedrinho tem um cofrinho com muitas moedas, e deseja saber quantos reais conseguiu poupar. Faça um 
#algoritmo para ler a quantidade de cada tipo de moeda, e imprimir o valor total economizado, em reais. 
#Considere que existam moedas de 1, 5, 10, 25 e 50 centavos, e ainda moedas de 1 real. Não havendo 
#moeda de um tipo, a quantidade respectiva é zero.