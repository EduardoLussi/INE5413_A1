from Q1_Grafo import *


def bellmanFord(grafo, origem):
    tamanho = grafo.qtdVertices()

    # Inicialização dos vetores
    d = [inf] * tamanho  # Distância com pesos (arestas ou arcos)
    a = [None] * tamanho  # Ancestral direto de v na árvore de largura (para essa questão, a árvore não é utilizada)

    d[origem - 1] = 0  # Distância do vértice de origem para ele mesmo é 0

    for i in range(0, tamanho-1):  # Percorre até o penúltimo elemento
        for aresta in grafo.arestas:  # Para cada aresta (u,v) do grafo
            u = aresta.vertices[0]
            v = aresta.vertices[1]
            # Processo de relaxamento
            if d[v.indice-1] > d[u.indice-1] + grafo.peso(u, v):  # Altera o valor se a distância até v é maior que a distância até u + peso da aresta (u,v)
                d[v.indice-1] = d[u.indice-1] + grafo.peso(u, v)
                a[v.indice-1] = u

    # Criação da mensagem de saída
    saida = ""
    for i in range(0, tamanho):
        v = grafo.vertices[i]
        saida += f"{v.indice}: {listarAncestrais(v, a)[:-1]}; d={d[v.indice-1]} \n"
    print(saida)


# Função auxiliar para criar a mensagem de saída
def listarAncestrais(origem, ancestrais):
    ancestralAtual = ancestrais[origem.indice - 1]
    if ancestralAtual is None:
        return origem.rotulo + ","
    else:
        return listarAncestrais(ancestralAtual, ancestrais) + origem.rotulo + ","


grafo = Grafo()
grafo.ler("GrafosTeste/fln_pequena.net")   # Diretório do arquivo do grafo
bellmanFord(grafo, 1)