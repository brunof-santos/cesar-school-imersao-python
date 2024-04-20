# Atividade 1
# letra = input("Digite a letra: ")
# if letra == "c" or letra == "C":
#     print("Casado")
# elif letra == "s" or letra =="S":
#     print("Solteiro")
# elif letra == "v" or letra == "V":
#     print("Viúvo")
# elif letra == "d" or letra == "D":
#     print("Divorciado")
# else:
#     print("Entrada inválida!")

# Atividade 2
# codigo = int(input("Digite o código do cargo: "))
# salarioAtual = float(input("Digite o salário atual: "))
# if codigo == 1:
#     aumento = 45
# elif codigo == 2:
#     aumento = 35
# elif codigo == 3:
#     aumento = 25
# elif codigo == 4:
#     aumento = 15
# else:
#     aumento = 0
# salarioAtualizado = salarioAtual*(1+aumento/100)
# print(f"Salário atualizado: {salarioAtualizado}")

# Atividade 3
# numDia = int(input("Digite o número do dia da semana: "))
# if numDia == 1:
#     print("Domingo")
# elif numDia == 2:
#     print("Segunda")
# elif numDia == 3:
#     print("Terça")
# elif numDia == 4:
#     print("Quarta")
# elif numDia == 5:
#     print("Quinta")
# elif numDia == 6:
#     print("Sexta")
# elif numDia == 7:
#     print("Sábado")
# else:
#     print("Valor Inválido")

# Atividade 4
# numInfracoes = int(input("Digite quantas infrações foram cometidas no último ano: "))
# if numInfracoes == 0:
#     print("Categoria: Motorista Exemplar")
# elif numInfracoes > 0 and numInfracoes <= 3:
#     print("Categoria: Motorista Atento")
# elif numInfracoes > 3 and numInfracoes <= 6:
#     print("Categoria: Motorista Desatento")
# elif numInfracoes > 6:
#     print("Categoria: Motorista Perigoso")
# else:
#     print("Número inválido")

# Atividade 5
# tipoSuite = int(input("Digite o tipo da suíte (1.Standar/2.Luxo/3.Presidencial: "))
# numNoites = int(input("Digite a quantidade de noites da hospedagem: "))
# if tipoSuite == 1:
#     custo = 250
#     limite = 15
# elif tipoSuite == 2:
#     custo = 500
#     limite = 10
# elif tipoSuite == 3:
#     custo = 1200
#     limite = 7
# else:
#     custo = 0
#     limite = 0
#
# if limite == 0:
#     print("Tipo de suíte inválido")
# elif limite != 0 and numNoites > limite:
#     print("Limite de noites atingido.")
# else:
#     if numNoites >= 5:
#         desconto = 10
#     else:
#         desconto = 0
#     valorTotal = custo * numNoites * (1 - desconto/100)
#     print(f"Valor total da estadia: R$ {valorTotal}")

# Atividade 6
# tipoSessao = int(input("Digite o tipo da sessão (1.Matinê/2.Vespertina/3.Noturna): "))
# idade = int(input("Digite a idade do cliente: "))
# if 12 < idade < 65:
#     estudante = input("Digite se o cliente é estudante (S/N): ")
#     if estudante == "S" or estudante == "s":
#         desconto = 50
#     else:
#         desconto = 0
# else:
#     desconto = 50
#
# if tipoSessao == 1:
#     valor = 20
# elif tipoSessao == 2:
#     valor = 25
# elif tipoSessao == 3:
#     valor = 30
# else:
#     valor = 0
#
# if valor == 0:
#     print("Tipo da sessão inválida")
# else:
#     valorFinal = valor * (1 - desconto/100)
#     print(f"Valor do ingresso: R$ {valorFinal}")

# Atividade 7
VALOR_MIN_EXCEDIDO = 1
VALOR_GB_EXCEDIDO = 10
print("Veja os planos abaixo:")
print("Plano Básico: 100 minutos e 5GB de internet por R$ 50")
print("Plano Intermediário: 300 minutos e 10GB de internet por R$ 80")
print("Plano Avançado: 500 minutos e 20GB de internet por R$ 120")
plano = input("\nEscolha um plano: ")
# não vou fazer as verificações e correções não, se errar o português errou, tô cansado
usoMinutos = int(input("Digite quantos minutos o cliente usou: "))
usoBanda = int(input("Digite quantos GB de banda o cliente usou: "))
if plano == "Básico":
    limiteMinutos = 100
    limiteBanda = 5
    valor = 50
elif plano == "Intermediário":
    limiteMinutos = 300
    limiteBanda = 10
    valor = 80
elif plano == "Avançado":
    limiteMinutos = 500
    limiteBanda = 20
    valor = 120
else:
    limiteMinutos = 0
    limiteBanda = 0
    valor = 0

if valor == 0:
    print("Plano inválido")
else:
    minutosExcedentes = 0
    if usoMinutos > limiteMinutos:
        minutosExcedentes = usoMinutos - limiteMinutos

    gbExcedentes = 0
    if usoBanda > limiteBanda:
        gbExcedentes = usoBanda - limiteBanda
    valorFatura = valor + minutosExcedentes * VALOR_MIN_EXCEDIDO + gbExcedentes * VALOR_GB_EXCEDIDO
    print(f"Valor total da fatura: R$ {valorFatura:.2f}")
