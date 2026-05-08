altura_pessoa = float(input("Digite sua altura: "))
sombra_pessoa = float(input("Digite o comprimento da sua sombra: "))
sombra_predio = float(input("Digite o comprimento da sombra do predio: "))
altura_predio = (altura_pessoa * sombra_predio) / sombra_pessoa

print(f"A altura do predio é de: {altura_predio} metros")

#Num dia de sol, você deseja medir a altura de um prédio, porém, a trena não é suficientemente longa. 
#Assumindo que seja possível medir sua sombra e a do prédio no chão, e que você lembre da sua altura, 
#faça um algoritmo para ler os dados necessários e calcular a altura do prédio.