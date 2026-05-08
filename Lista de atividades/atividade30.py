salario_fixo = float(input("Digite o salário fixo: R$ "))
vendas = float(input("Digite o valor das vendas: R$ "))

comissao = vendas * 0.04
salario_final = salario_fixo + comissao

print(f"Comissão: R$ {comissao:.2f}")
print(f"Salário Final: R$ {salario_final:.2f}")

#Um funcionário recebe um salário fixo mais 4% de comissão sobre as vendas. Faça um algoritmo que 
#receba o salário fixo de um funcionário e o valor de suas vendas, calcule e mostre a comissão e o 
#salário final do funcionário.