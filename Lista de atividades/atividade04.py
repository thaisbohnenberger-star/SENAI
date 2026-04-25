nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

if idade > 120 or idade <0:
    print("Idade inválida! por favor, digite um valor menor ou igual a 120 ou maior que 0.")
else:

    dias_de_vida = idade * 365
    print(f"Olá {nome}, voce já viveu cerca de: {dias_de_vida}")
#Escreva um algoritmo para ler o nome e a idade de uma pessoa, e exibir quantos dias de vida ela 
# possui. Considere sempre anos completos, e que um ano possui 365 dias. Ex: uma pessoa com 19 anos 
# possui 6935 dias de vida; veja um exemplo de saída: MARIA, VOCÊ JÁ VIVEU 6935 DIAS 