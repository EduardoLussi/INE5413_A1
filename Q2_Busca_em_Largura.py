from Q1_Grafo import *
import queue


def buscaLargura(grafo, origem):

    tamanho = grafo.qtdVertices()

    # Inicialização dos vetores
    c = [False] * tamanho  # Conhecidos
    d = [inf] * tamanho  # Distância (arestas ou arcos)
    a = [None] * tamanho  # Ancestral direto de v na árvore de largura (para essa questão, a árvore não é utilizada)

    # Configurando o vértice de origem
    c[origem-1] = True
    d[origem-1] = 0

    # Criação e inicialização da fila de visitas
    fila = queue.Queue()
    fila.put(grafo.obterVertice(origem))

    # Propagação das visitas
    while not(fila.empty()):
        aux = fila.get()
        n = grafo.vizinhos(aux)
        for v in n:
            vIndex = v.indice - 1
            auxIndex = aux.indice - 1
            if not(c[vIndex]):
                c[vIndex] = True
                d[vIndex] = d[auxIndex] + 1
                a[vIndex] = auxIndex + 1
                fila.put(v)

    flag = True  # Define se a distância máxima já foi alcançada (ignorando o infinito)
    distancia = 0
    saida = ""

    # Procedimento de impressão do resultado em níveis
    while flag:
        flag = False
        for i in range(0, tamanho):
            if d[i] == distancia:
                if not flag:
                    flag = True
                    saida += f"\n{distancia}: {i+1}"
                else:
                    saida += f",{i+1}"
        distancia += 1

    print(saida)
