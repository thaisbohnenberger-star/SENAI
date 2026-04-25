camisa_pequena= int(input("Digite a quantia de camisetas pequenas você comprou: "))
camisa_medio = int(input("Digite a quantia de camisetas médias você comprou: "))
camisa_grande = int(input("Digite a quantia de camisetas grandes você comprou: "))

pequeno = camisa_pequena * 10
medio = camisa_medio * 12
grande = camisa_grande * 15

total = pequeno + medio + grande

print("O valor total arrecadado foi de: R$",total)
#Uma fábrica de camisetas produz os tamanhos pequeno, médio e grande, cada uma sendo vendida 
# respectivamente por 10, 12 e 15 reais. Construa um algoritmo em que o usuário forneça a quantidade 
# de camisetas pequenas, médias e grandes referentes a uma venda, e a máquina informe quanto será o 
# valor arrecadado. 