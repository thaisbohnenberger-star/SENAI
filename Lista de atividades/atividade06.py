while True:
    peso_prato = int(input("Escreva o peso do seu prato (Kg): "))
    if peso_prato >= 0:
        break
    print("Valor Inválido")

total = peso_prato * 12
print("O valor total é de : R$",total)
#O restaurante a quilo Bem-Bão cobra R$12,00 por cada quilo de refeição. Escreva um algoritmo que leia 
# o peso do prato montado pelo cliente (em quilos) e imprima o valor a pagar. Assuma que a balança já 
# desconte o peso do prato. 