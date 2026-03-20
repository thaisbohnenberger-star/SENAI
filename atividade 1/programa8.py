nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

if idade <=0:
    print("Inválido, digite novamente: ")
elif idade >=116:
    print("Inválido, digite novamente: ")
else:
    dias = (idade * 365)
    print(nome,"você já viveu", dias,"dias")
