from Q1_Grafo import Grafo


def printSolution(D):   # Exibe solução
    for i, vDist in enumerate(D):
        text = f"{i+1}:"
        for dist in vDist:
            text += f"{dist},"
        print(text[:-1])


def FloydWarshall(grafo):
    D = []
    for u in grafo.vertices:    # Monta matriz D de adjacências
        Di = []
        for v in grafo.vertices:
            Di.append(grafo.peso(u, v))
        D.append(Di)

    for ki, k in enumerate(grafo.vertices): # Executa o algoritmo
        for ui, u in enumerate(grafo.vertices):
            for vi, v in enumerate(grafo.vertices):
                # Tenta inserir vértice k no caminho entre u e v
                D[ui][vi] = min(D[ui][vi], D[ui][ki] + D[ki][vi])

    printSolution(D)


grafo = Grafo()
grafo.ler("GrafosTeste/fln_pequena.net")   # Diretório do arquivo do grafo
FloydWarshall(grafo)