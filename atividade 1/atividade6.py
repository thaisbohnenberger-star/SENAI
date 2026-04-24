while True:
    peso_prato = int(input("Escreva o peso do seu prato (Kg): "))
    if peso_prato >= 0:
        break
    print("Valor Inválido")

total = peso_prato * 12
print("O valor total é de : R$",total)
