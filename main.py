# Transformação AFε -> AFN

print("=" * 50)
print("TRANSFORMACAO DE AFε PARA AFN")
print("=" * 50)

# Estados
estados = input("Informe os estados do automato: ").replace(" ", "").split(",")

# Estado inicial
estado_inicial = input("Informe o estado inicial: ").strip()

# Quantidade de transições
qtd_transicoes = int(input("Quantidade de transicoes: "))

# Função programa
transicoes = []

print("\nInforme as transicoes:")

for i in range(qtd_transicoes):
    transicao = input(f"Transicao {i+1}: ")
    transicoes.append(transicao)

# Estados finais
estados_finais = input(
    "\nInforme os estados finais: "
).replace(" ", "").split(",")

print("\n--- DADOS INFORMADOS ---")
print("Estados:", estados)
print("Estado inicial:", estado_inicial)
print("Transicoes:", transicoes)
print("Estados finais:", estados_finais)