class Vertice:
    def __init__(self, indice, rotulo, E):
        self.indice = indice
        self.rotulo = rotulo
        self.E = E  # Lista de dicionário {"V": Vertice, "peso": peso}

    # Retorna o grau do vértice
    def grau(self):
        ...

    # Retorna os vizinhos
    def vizinhos(self):
        ...

    # Se houver aresta com V, retorna verdadeiro, senão, retorna falso
    def haAresta(self, V):
        ...

    # Retorna peso da aresta com V, se não existir, retorna infinito positivo
    def peso(self, V):
        ...


class Grafo:
    def __init__(self, V):
        self.V = V

    # Retorna a quantidade de vértices
    def qtdVertices(self):
        return len(self.V)

    # Retorna a quantidade de arestas
    def qtdArestas(self):
        ...

    # Retorna o grau do vértice V
    def grau(self, V):
        ...

    # Retorna o rótulo do vértice V
    def rotulo(self, V):
        ...

    # Retorna os vizinhos de V
    def vizinhos(self, V):
        ...

    # Se existe aresta entre U e V, retorna verdadeiro, senão, retorna falso
    def haAresta(self, U, V):
        ...

    # Retorna o peso da aresta {U, V}, se não existir, retorna infinito positivo
    def peso(self, U, V):
        ...

    # Carrega um grafo a partir de um arquivo
    def ler(self, arquivo):
        ...
