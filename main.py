# ==================================================
# Universidade Federal do Maranhão (UFMA)
# Centro de Ciências Exatas e Tecnologia
# Curso de Engenharia da Computação
# Disciplina: Linguagens Formais e Autômatos
#
# Discente: Renata Costa Rocha
#
# Implementação do algoritmo de transformação
# AFε -> AFN
# ==================================================


def ler_lista(mensagem):
    entrada = input(mensagem).replace(" ", "")

    if entrada == "":
        return []

    return entrada.split(",")


def ler_transicoes():
    transicoes = []

    print("\nInforme a função programa:")
    print("Digite uma transição por linha.")
    print("Exemplo: 0a1 ou 0ε2")
    print("Pressione ENTER vazio para finalizar.\n")

    while True:
        if len(transicoes) == 7:
            print("Limite de 7 transições atingido.")
            break

        transicao = input("Transição: ").replace(" ", "")

        if transicao == "":
            break

        if len(transicao) != 3:
            print("Erro: a transição deve ter o formato origem simbolo destino. Exemplo: 0a1")
            continue

        transicoes.append(transicao)

    return transicoes


def validar_entrada(estados, estado_inicial, transicoes, estados_finais):
    if len(estados) > 5:
        print("Erro: o AFε deve possuir no máximo 5 estados.")
        return False

    if len(transicoes) > 7:
        print("Erro: o AFε deve possuir no máximo 7 transições.")
        return False

    if estado_inicial not in estados:
        print("Erro: o estado inicial deve pertencer ao conjunto de estados.")
        return False

    for estado_final in estados_finais:
        if estado_final not in estados:
            print("Erro: todos os estados finais devem pertencer ao conjunto de estados.")
            return False

    for transicao in transicoes:
        origem = transicao[0]
        simbolo = transicao[1]
        destino = transicao[2]

        if origem not in estados or destino not in estados:
            print("Erro: origem e destino das transições devem pertencer ao conjunto de estados.")
            return False

    alfabeto = obter_alfabeto(transicoes)

    if len(alfabeto) > 3:
        print("Erro: o alfabeto deve possuir no máximo 3 símbolos.")
        return False

    return True


def calcular_epsilon_fecho(estado, transicoes):
    fecho = {estado}
    pilha = [estado]

    while pilha:
        atual = pilha.pop()

        for transicao in transicoes:
            origem = transicao[0]
            simbolo = transicao[1]
            destino = transicao[2]

            if origem == atual and simbolo == "ε":
                if destino not in fecho:
                    fecho.add(destino)
                    pilha.append(destino)

    return fecho


def obter_alfabeto(transicoes):
    alfabeto = set()

    for transicao in transicoes:
        simbolo = transicao[1]

        if simbolo != "ε":
            alfabeto.add(simbolo)

    return alfabeto


def gerar_transicoes_afn(estados, transicoes, fechos, alfabeto):
    novas_transicoes = set()

    for estado in estados:
        for simbolo in alfabeto:
            destinos = set()

            for estado_fecho in fechos[estado]:
                for transicao in transicoes:
                    origem = transicao[0]
                    simbolo_transicao = transicao[1]
                    destino = transicao[2]

                    if origem == estado_fecho and simbolo_transicao == simbolo:
                        destinos.update(fechos[destino])

            for destino in destinos:
                novas_transicoes.add((estado, simbolo, destino))

    return novas_transicoes


def gerar_estados_finais_afn(estados, estados_finais, fechos):
    novos_finais = set()

    for estado in estados:
        for estado_fecho in fechos[estado]:
            if estado_fecho in estados_finais:
                novos_finais.add(estado)
                break

    return novos_finais


def imprimir_conjunto(nome, conjunto):
    if len(conjunto) == 0:
        print(f"{nome}: vazio")
    else:
        print(f"{nome}: " + ", ".join(sorted(conjunto)))


print("=" * 50)
print("TRANSFORMAÇÃO DE AFε PARA AFN")
print("=" * 50)

print("\nRestrições:")
print("- O AFε deve possuir no máximo 5 estados.")
print("- O AFε deve possuir no máximo 7 transições.")
print("- O alfabeto deve possuir no máximo 3 símbolos.")

estados = ler_lista("\nInforme os estados do autômato: ")
estado_inicial = input("Informe o estado inicial: ").strip()
transicoes = ler_transicoes()
estados_finais = ler_lista("\nInforme os estados finais: ")

if not validar_entrada(estados, estado_inicial, transicoes, estados_finais):
    print("\nPrograma encerrado devido a erro na entrada.")
    exit()

print("\n" + "-" * 50)
print("DADOS INFORMADOS")
print("-" * 50)

imprimir_conjunto("Estados", estados)
print("Estado inicial:", estado_inicial)
print("Transições:", transicoes)
imprimir_conjunto("Estados finais", estados_finais)

fechos = {}

print("\n" + "-" * 50)
print("ε-FECHOS")
print("-" * 50)

for estado in estados:
    fechos[estado] = calcular_epsilon_fecho(estado, transicoes)
    print(
        f"ε-fecho({estado}) = "
        + "{"
        + ", ".join(sorted(fechos[estado]))
        + "}"
    )

alfabeto = obter_alfabeto(transicoes)

novas_transicoes = gerar_transicoes_afn(
    estados,
    transicoes,
    fechos,
    alfabeto
)

novos_finais = gerar_estados_finais_afn(
    estados,
    estados_finais,
    fechos
)

print("\n" + "=" * 50)
print("AFN EQUIVALENTE")
print("=" * 50)

print("\nEstado inicial:")
print(estado_inicial)

print("\nEstados finais:")
print(", ".join(sorted(novos_finais)))

print("\nTransições:")

for origem, simbolo, destino in sorted(novas_transicoes):
    print(f"{origem}{simbolo}{destino}")