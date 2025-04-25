# Exercício 5
nota1 = float(input("Digite a nota da primeira avaliação: "))
nota2 = float(input("Digite a nota da segunda avaliação: "))
nota_optativa = float(input("Digite a nota da avaliação optativa (-1 se não fez): "))

if nota_optativa != -1:
    if nota1 < nota2:
        nota1 = nota_optativa
    else:
        nota2 = nota_optativa

media = (nota1 + nota2) / 2

if media >= 6.0:
    situacao = "Aprovado"
elif media < 3.0:
    situacao = "Reprovado"
else:
    situacao = "Exame"

print(f"Média do semestre: {media:.1f}")
print(f"Situação: {situacao}")