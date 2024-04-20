# Atividade 1
# idade = 0
# i = 0
# somaIdades = 0
# maior = 0
# menor = 0
# media = 0
# while idade != -1:
#     idade = int(input("Digite uma idade ou -1 para finalizar: "))
#     if idade != -1:
#         if idade >= 25:
#             maior += 1
#         else:
#             menor += 1
#         somaIdades += idade
#         i = i + 1
# media = somaIdades/i
# print(f"Total de idades: {i} \nMédia das idades: {media} \nMaiores de 25 anos: {maior} \nMenores de 25 anos: {menor}")

# Atividade 2
# nota = 0
# soma = 0
# total = 0
#
# while nota != -1:
#     nota = int(input("Digite uma nota de 1 a 5: "))
#     if not (1 <= nota <= 5):
#         print("Nota inválida!")
#     else:
#         soma += nota
#         total += 1
# media = soma/total
# print(f"Média das notas: {media}")

# Atividade 3
# quantidade = 0
# tipo = 0
# nome = "segue"
# while nome != "FIM":
#     nome = input("Digite o nome do produto: ")
#     if nome == "FIM":
#         continue
#     quantidade = int(input("Digite a quantidade do produto: "))
#     if quantidade < 0:
#         print("Não é possível cadastro de estoque negativo.")
#     else:
#         tipo += 1
# print(f"Tipos de produtos cadastrados: {tipo}")

# Atividade 4
# codigo = 0
# atendimentos = 0
# quantidadeBanho = 0
# quantidadeTosa = 0
# quantidadeBanhoETosa = 0
# quantidadeOutros = 0
# while atendimentos <= 9:
#     codigo = int(input("Digite o código do serviço: "))
#     if codigo == 1:
#         quantidadeBanho += 1
#     elif codigo == 2:
#         quantidadeTosa += 1
#     elif codigo == 3:
#         quantidadeBanhoETosa += 1
#     elif codigo == 4:
#         quantidadeOutros += 1
#     atendimentos += 1
# print(f"Banho: {quantidadeBanho} \nTosa: {quantidadeTosa} \nBanho e tosa: {quantidadeBanhoETosa} \nOutros: {quantidadeOutros}")

# Atividade 5
