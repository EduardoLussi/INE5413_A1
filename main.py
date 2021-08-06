from Q1_Grafo import *
from Q2_Busca_em_Largura import *
from Q3_Ciclo_Euleriano import *
from Q4_BellmanFord import *
from Q5_FloydWarshall import *

# Exemplo de Grafo
print("\nExemplo de execução - Questão 1\n")
grafo = Grafo()
grafo.ler("GrafosTeste/facebook_santiago.net")
print(grafo.obterVertice(200).rotulo)

# Exemplo de Busca em Largura
print("\nExemplo de execução - Questão 2\n")
grafo = Grafo()
grafo.ler("GrafosTeste/grafo_teste.net")
buscaLargura(grafo, 1)

# Exemplo Ciclo Euleriano
print("\nExemplo de execução - Questão 3\n")
grafo = Grafo()
grafo.ler("GrafosTeste/ContemCicloEuleriano.net")   # Diretório do arquivo do grafo
CicloEuleriano(grafo)

# Exemplo Bellman Ford
print("\nExemplo de execução - Questão 4\n")
grafo = Grafo()
grafo.ler("GrafosTeste/fln_pequena.net")   # Diretório do arquivo do grafo
bellmanFord(grafo, 1)

# Exemplo Floyd Warshall
print("\nExemplo de execução - Questão 5\n")
grafo = Grafo()
grafo.ler("GrafosTeste/fln_pequena.net")   # Diretório do arquivo do grafo
FloydWarshall(grafo)