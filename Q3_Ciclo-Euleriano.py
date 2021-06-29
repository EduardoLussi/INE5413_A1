from Q1_Grafo import Grafo


def buscarSubcicloEuleriano(grafo, v, C):
    text = f"Função auxiliar: v={v.rotulo}, C={[c.rotulo for c in C]}"
    print(text)

    Ciclo = [v]
    t = v

    while True:
        print(f"Vizinhos de {v.rotulo}: {[viz.rotulo for viz in grafo.vizinhos(v)]}")
        if len(C) == len(grafo.arestasVizinhos(v)): # Pode ter algo aqui
            print("Não existe aresta não-visitada conectada a Ciclo")
            return False, None

        for aresta in grafo.arestasVizinhos(v):
            if aresta not in C:
                # Redefine v
                if v == aresta.vertices[0]:
                    v = aresta.vertices[1]
                else:
                    v = aresta.vertices[0]

                C.append(aresta)

                break

        Ciclo.append(v)
        print(f"Ciclo: {[ver.rotulo for ver in Ciclo]}")

        if v == t:
            break

    naoVistadas = []
    for x in Ciclo:
        for aresta in grafo.arestasVizinhos(x):
            if aresta not in C:
                naoVistadas.append(aresta)

    for x in naoVistadas:
        r, Ciclo2 = buscarSubcicloEuleriano(grafo, x, C)
        if r is False:
            return False, None

        for i, v in enumerate(Ciclo):
            if v == x:
                Ciclo.insert(i+1, x)
                for u in Ciclo2[::-1]:
                    Ciclo.insert(i+1, u)

    return True, Ciclo


def Hierholzer(grafo):
    C = []

    v = grafo.vertices[0]

    r, Ciclo = buscarSubcicloEuleriano(grafo, v, C)

    if r is False:
        return False, None

    return True, Ciclo


grafo = Grafo()
grafo.ler("grafo_teste.net")

flag, c = Hierholzer(grafo)

if flag:
    print(1)

    cs = ''
    for v in c:
        cs += f"{v.rotulo} "
    print(cs)
else:
    print(0)


