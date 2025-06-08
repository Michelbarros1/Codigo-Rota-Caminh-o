import networkx as nx

G = nx.Graph()

# Conexões simuladas entre os centros de distribuição das 5 regiões brasileiras a as capitais dos estados, com tempo de viagem estimado (em horas)

caminhos = [
    ("Belém","Manaus",18),
    ("Belém","Rio Branco", 48),
    ("Belém","Porto Velho", 40),
    ("Belém","Boa Vista", 22),
    ("Belém","Macapá", 6),
    ("Belém","Palmas", 32),

    ("Recife","São Luís", 48),
    ("Recife","Teresina", 42),
    ("Recife","Fortaleza", 22),
    ("Recife","Natal", 8),
    ("Recife","João Pessoa", 4),
    ("Recife", "Maceió", 5),
    ("Recife", "Aracaju", 10),
    ("Recife", "Salvador", 16),

    ("Brasília","Goiania", 5),
    ("Brasília","Cuiabá", 9),
    ("Brasília", "Campo Grande", 12),

    ("São Paulo","Belo Horizonte", 8),
    ("São Paulo","Rio de Janeiro", 4),
    ("São Paulo","Vitória", 14),

    ("Florianópolis","Curitiba", 6),
    ("Florianópolis","Porto Alegre", 12),
]

G.add_weighted_edges_from(caminhos)

centros = ["Belém", "Recife", "Brasília", "São Paulo", "Florianópolis"]

# Pricipais Clientes e Demandas 
clientes = {
    "ExpressoAmazonasLDTA(AM)": 170,
    "Soluções_BaianasBR(BA)": 350,
    "MetaisFederais(GO)": 279,
    "BRAZILEXPRESS(SP)": 568,
    "FundaçãoSigmaBrasil": 450,
    "Companhia Nacional de Alimentos(CNA)": 599,
    "FundaçãoHuszAnthony(SC)": 666,
    "TransportesIrmãosMontero": 890,
    "LojasMarajoara(RO)": 355,
    "Companhia Metropolitana de São Paulo": 269,
    "MAXTITANIUM ltda": 958,

}

G.add_weighted_edges_from([
    ("ExpressoAmazonasLDTA(AM)", "Belém", 12),
    ("Soluções_BaianasBR(BA)", "Recife", 8),
    ("BRAZILEXPRESS(SP)", "São Paulo", 6),
    ("FundaçãoHuszAnthony(SC)","Florianópolis", 5),
    ("MetaisFederais(GO)", "Brasília", 10),
    ("FundaçãoSigmaBrasil", "Rio de Janeiro", 4),
    ("Companhia Nacional de Alimentos(CNA)", "Curitiba", 6),
    ("TransportesIrmãosMontero","Rio Branco", 2),
    ("LojasMarajaora(RO)", "Porto Velho", 2),
    ("MAXTITANIUM ltda","Porto Alegre", 8 ),
])

#  Parâmetros do caminhão 
capacidade_max = 600  # kg
tempo_max = 40        # horas


def centro_mais_proximo(destino):
    tempos = []
    for centro in centros:
        try:
            tempo = nx.dijkstra_path_length(G, centro, destino)
            tempos.append((centro, tempo))
        except nx.NetworkXNoPath:
            continue
    return min(tempos, key=lambda x: x[1]) if tempos else (None, float('inf'))
print("OLÁ, SEJA BEM VINDO (A) AQUI ESTÁ AS INFORMAÇÕES NECESSÁRIAS PARA O RELATÓRIO EMPRESARIAL:")

def simular_entregas():
    for cliente, demanda in clientes.items():
        print(f"\n📦 Cliente: {cliente} | Demanda: {demanda} kg")

        if demanda > capacidade_max:
            print(f"❌ Excede a capacidade do caminhão ({demanda} > {capacidade_max})")
            continue

        centro, tempo = centro_mais_proximo(cliente)
        if not centro:
            print("❌ Nenhum centro acessível")
            continue

        if tempo > tempo_max:
            print(f"❌ Tempo excedido ({tempo} > {tempo_max})")
            continue

        caminho = nx.dijkstra_path(G, centro, cliente)
        print(f"✅ Entrega possível!")
        print(f"🚚 Centro de saída: {centro}")
        print(f"🛣️ Rota: {' -> '.join(caminho)}")
        print(f"⏱️ Tempo estimado: {tempo}h")

if __name__ == "__main__":
    simular_entregas()
print("AS CINCO ROTAS ACIMA ESTÃO INCORRETAS, VERIFIQUE COM O CLIENTE O VOLUME DA CARGA OU O CENTRO DE DISTRIBUIÇÃO! ")