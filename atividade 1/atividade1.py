nome = input("Insira o seu nome: ")
nota1 = float(input("Insira sua primeira nota: "))
nota2 = float(input("Insira sua segunda nota: "))
media = (nota1 + nota2) /2
if media >= 7:
    print("O aluno está aprovado!")
else:
    print("O aluno está reprovado!")
    print("A média das notas é: ", media)
