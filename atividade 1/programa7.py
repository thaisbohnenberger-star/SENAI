quant_pao = int(input("Escreva a quantia de pão vendida: "))
quant_broas = int(input("Escreva a quantia de broas vendida: "))

arrecadado = (quant_pao * 0.12) + (quant_broas * 1.50)
poupança = (arrecadado * 0.10)

print("O total de vendas de pão e broas foi: ",arrecadado)
print("Você deve guardar", poupança,"na poupança")
