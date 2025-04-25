# Exercício 4 - Escreva um programa que leia o código de origem de um 
# produto e imprima na tela a região de sua procedência, conforme 
# a tabela abaixo:
# Observação: caso o código não seja nenhum dos especificados, o 
# produto deve ser encarado como “Importado”.

codigo = int(input("Digite o código de origem do produto: "))

if codigo == 1:
    regiao = "Sul"
elif codigo == 2:
    regiao = "Norte"
elif codigo == 3:
    regiao = "Leste"
elif codigo == 4: 
    regiao = "Oeste"
elif codigo == 5 or codigo == 6:
    regiao = "Nordeste"
elif codigo in [7,8.9]:
    regiao = "Sudeste"
elif 10 <= codigo <= 20:
    regiao = "Centro-Oeste"
elif 21 <= codigo <=30:
    regiao = "Nordeste"
else:
    regiao = "Importado"
print(f"A região de procedência do produto é {regiao}")