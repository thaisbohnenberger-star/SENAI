total_refresco = float(input("Quantidade de refresco desejada (litros): "))

agua = total_refresco * 0.8  # 8 partes de 10
suco = total_refresco * 0.2  # 2 partes de 10

print(f"Para {total_refresco}L de refresco, use {agua:.2f}L de água e {suco:.2f}L de suco.")

#Um tonel de refresco é feito com 8 partes de água mineral e 2 partes de suco de maracujá. Faça um 
#algoritmo para calcular quantos litros de água e de suco são necessários para se fazer X litros de 
#refresco (informados pelo usuário).