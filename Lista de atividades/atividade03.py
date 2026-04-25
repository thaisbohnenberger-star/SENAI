quant_pao = int(input("Escreva a quantia de pão vendida: "))
quant_broas = int(input("Escreva a quantia de broas vendida: "))

arrecadado = (quant_pao * 0.12) + (quant_broas * 1.50)
poupança = (arrecadado * 0.10)

print("O total de vendas de pão e broas foi: ",arrecadado)
print("Você deve guardar", poupança,"na poupança")
#A padaria Hotpão vende uma certa quantidade de pães franceses e uma quantidade de broas a cada dia.
# Cada pãozinho custa R$ 0,12 e a broa custa R$ 1,50. Ao final do dia, o dono quer saber quanto 
# arrecadou com a venda dos pães e broas (juntos), e quanto deve guardar numa conta de poupança 
# (10% do total arrecadado). Você foi contratado para fazer os cálculos para o dono. Com base nestes 
# fatos, faça um algoritmo para ler as quantidades de pães e de broas, e depois calcular os dados 
# solicitados. 