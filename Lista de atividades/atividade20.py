qtd_blusas = int(input("Digite a quantidade de blusas que você deseja: "))
metros_totais = qtd_blusas * 120
novelos = metros_totais // 125

if metros_totais % 125 > 0:
    novelos += 1

print(f"Total de novelos necessários: {novelos}")

#Como calcular a quantidade de novelos de lã necessários para produzir cada blusa em uma confecção, 
#considerando que cada blusa requer uma quantidade de 120 metros de fio e que cada novelo contém 125 
#de metros de fio?