PI = 3.14

# Atividade 1
graus = float(input("Digite o ângulo em graus: ")) #tipo int pra facilitar a saída e a resposta ficar igual, mas deveria ser float
radianos = graus*PI/180
print(f"{graus:.2f} graus em radianos é {radianos:.2f}.\n")

# Atividade 2
valorOriginal = float(input("Insira o valor original do produto: "))
desconto = float(input("Insira a porcentagem de desconto (%): "))
valorComDesconto = valorOriginal*(1-desconto/100)
print(f"Valor com desconto: R$ {valorComDesconto}\n")
#print(f"Valor com desconto: R$ {valorComDesconto:.2f}\n")

# Atividade 3
ladoA = float(input("Digite o comprimeiro do lado A: "))
ladoB = float(input("Digite o comprimeiro do lado B: "))
ladoC = float(input("Digite o comprimeiro do lado C: "))
s = (ladoA + ladoB + ladoC)/2
area = (s*(s-ladoA)*(s-ladoB)*(s-ladoC))**0.5
if not (ladoA + ladoB > ladoC and ladoA + ladoC > ladoB and ladoB + ladoC > ladoA):
    print(f"OBS: Triângulo impossível")
print(f"Área do triângulo: {area}\n")

# Atividade 4
valorInicial = float(input("Digite o valor inicial: "))
taxaJuros = float(input("Digite a taxa de juros (%): "))
tempo = int(input("Digite o tempo (em anos): "))

valorFuturo = valorInicial * (1 + taxaJuros/100 * tempo)
print(f"Valor futuro: {valorFuturo:.1f}\n")
#print(f"Valor futuro: {valorFuturo:.2f}\n")

# Atividade 5
valorVendas = float(input("Digite o valor total das vendas: "))
porcentagemComissao = float(input("Digite a porcentagem de comissão: "))
comissao = valorVendas * porcentagemComissao/100
print(f"Valor da Comissão: R$ {comissao:.2f}\n")

# Atividade 6
raio = float(input("Digite o raio do círculo: "))
area = PI*raio**2
print(f"Área do círculo: {area:.1f}.\n")

# Atividade 7
valorCusto = float(input("Digite o custo de produção do produto: "))
valorVenda = float(input("Digite o valor de venda do produto: "))
lucroBruto = valorVenda - valorCusto
print(f"Lucro Bruto: R$ {lucroBruto:.1f}\n")

# Atividade 8
celsius = int(input("Digite a temperatura em graus Celsius: ")) #tipo int pra facilitar a saída e a resposta ficar igual, mas deveria ser float
farenheit = celsius*9/5 + 32
print(f"{celsius} graus Celsius é {farenheit:.1f} graus Farenheit.\n")

# Atividade 9
valorProduto = float(input("Digite o valor do produto: "))
imposto = float(input("Digite a taxa do imposto (%): "))
valorFinal = valorProduto*(1+imposto/100)
print(f"Valor Final com Imposto: R$ {valorFinal:.1f}\n")
#print(f"Valor Final com Imposto: R$ {valorFinal:.2f}\n")

# Atividade 10
valorCompra = float(input("Digite o valor total da compra: "))
numeroParcelas = int(input("Digite o número de parcelas desejadas: "))
valorParcela = valorCompra/numeroParcelas
print(f"Valor de cada parcela: R$ {valorParcela}\n")
#print(f"Valor de cada parcela: R$ {valorParcela:.2f}\n")