from Q1_Grafo import Grafo


def buscarSubcicloEuleriano(grafo, v, C):
    Ciclo = [v] # Inicia ciclo com o primeiro vértice
    t = v   # Salva primeiro vértice

    while True:
        # Só prossegue se existir uma aresta não-visitada conectada a Ciclo
        # Transforma lista de arestas de v e visitadas C em um conjuntos e verifica se
        # as arestas de v estão contidas em C
        if set(grafo.arestasVizinhos(v)).issubset(set(C)):
            return False, None

        # Seleciona uma aresta não visitada
        for aresta in grafo.arestasVizinhos(v):
            if aresta not in C:
                # Redefine v -> vértice atual
                if v == aresta.vertices[0]:
                    v = aresta.vertices[1]
                else:
                    v = aresta.vertices[0]

                C.append(aresta)    # adiciona aresta a visitadas

                break

        Ciclo.append(v) # Adiciona vértice ao ciclo

        if v == t:  # Finaliza quando fechar o ciclo
            break

    # Verifica se há subciclos enquanto houver vértices que possuem arestas não visitadas
    while True:
        naoVisitado = -1
        for x in Ciclo: # Encontra vértice com aresta não visitada
            for aresta in grafo.arestasVizinhos(x):
                if aresta not in C:
                    naoVisitado = x
                    break
            if naoVisitado != -1:
                break

        if naoVisitado == -1:   # Todas as arestas foram visitadas
            break

        # Consulta se há subciclo
        r, Ciclo2 = buscarSubcicloEuleriano(grafo, naoVisitado, C)

        if r is False:
            return False, None  # Não há subciclo, grafo não possui ciclo euleriano

        for i, v in enumerate(Ciclo):   # Adiciona subciclo ao ciclo original
            if v == naoVisitado:
                for u in Ciclo2[1:]:
                    Ciclo.insert(i+1, u)
                    i += 1
                break

    return True, Ciclo


def Hierholzer(grafo):
    C = []  # C é uma lista de arestas

    v = grafo.vertices[0]   # Seleciona primeiro vértice

    r, Ciclo = buscarSubcicloEuleriano(grafo, v, C) # Busca ciclo euleriano a partir de v

    if r is False:
        return False, None

    return True, Ciclo


def CicloEuleriano(grafo):
    flag, c = Hierholzer(grafo)

    # Impressão de resultados
    if flag:
        print(1)

        cs = ''
        for v in c:
            cs += f"{v.rotulo},"
        print(cs[:-1])
    else:
        print(0)


grafo = Grafo()
grafo.ler("GrafosTeste/ContemCicloEuleriano.net")   # Diretório do arquivo do grafo
CicloEuleriano(grafo)