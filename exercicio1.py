# Exercício 2 -Escreva um programa para ler as dimensões de uma cozinha 
# retangular (comprimento, largura e altura), calcular e escrever a 
# quantidade de caixas de azulejos para se colocar em todas as 
# suas paredes (considere que não será descontada a área 
# ocupada por portas e janelas).
# Cada caixa de azulejos possui 1,5 m²

#Varivél inicial
largura = float(input('Informe a largura em metros:'))
comprimento = float(input('Informe o comprimento em metros:'))
altura = float(input('Informe a altura em metros:'))

#Variavél de cálculo
l_x_c_m2 = largura * comprimento
l_x_a_m2 = largura * altura
m2_t = l_x_a_m2 + l_x_c_m2
totalcaixas = round((m2_t / 1.5), 2)
print('Total de caixas:', totalcaixas)
