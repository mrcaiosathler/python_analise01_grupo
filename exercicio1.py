# EXERCÍCIO 1
# Escreva um programa para calcular e imprimir o número de lâmpadas necessárias para iluminar um determinado cômodo de uma residência. Dados de entrada: a potência da lâmpada utilizada (em watts), as dimensões (largura e comprimento, em metros) do cômodo. Considere que a potência necessária é de 3 watts por metro quadrado e a cada 3 m² existe um bocal para uma lâmpada.
# Calcular e escrever: o número de lâmpadas necessárias para iluminar um determinado cômodo de uma residência.

#Variáveis Iniciais
LarguraComodo = float(input("Informe a largura do cômodo: "))
ComprimentoComodo = float(input("Informe o comprimento do cômodo: "))
PotenciaLampada = float(input("Informe a potência das lâmapadas que você escolheu: "))

#Variáveis de Cálculo
MedidaQuarto = LarguraComodo*ComprimentoComodo
PotNecessaria = MedidaQuarto*3
QuantLampadas = round((PotNecessaria/PotenciaLampada), 0)

print("Você precisará de ", QuantLampadas, "lâmpadas para iluminar o cômodo.")



# EXERCÍCIO 3
# Um motorista de táxi deseja calcular o rendimento de seu carro na praça. Sabendo-se que o preço do combustível é de R$ 4,87, escreva um programa para ler: a marcação do odômetro (km) no início do dia, a marcação (km) no final do dia, o número de litros  de combustível gasto e o valor total (R$) recebido dos passageiros.
# Calcular e escrever: a média do consumo em km/L e o lucro (líquido) do dia.

#Variáveis Iniciais
kminic = float(input("Informe a quilometragem inicial do dia de hoje:"))
kmfim = float(input("Informe a quilometragem final do dia de hoje:"))
combgasto = float(input("Informe quantos litros de combustível você consumiu no dia de hoje:"))
valorrecebido = float(input("Informe o valor recebido dos passageiros no dia de hoje:"))

#Variáveis de Cálculo
kmdia = round((kmfim-kminic), 2)
mediakm = (kmdia/combgasto)
lucrodia = (round((valorrecebido - (kmdia*4.87)),2))

#Resultados
print("A sua média de consumo hoje foi de ", mediakm, "km/L, enquanto seu lucro foi de R$", lucrodia)
