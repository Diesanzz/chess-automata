import networkx as nx
import matplotlib.pyplot as plt


def construir_red_j1(nfa, inicio, cadena):

    red = []  # lista de aristas
    nodos = set()

    actuales = [(inicio, 0)]
    nodos.add((inicio, 0))

    for i, simbolo in enumerate(cadena):

        nuevos = []

        for (estado, nivel) in actuales:

            for sig in nfa[estado][simbolo]:

                nodo_siguiente = (sig, i+1)

                red.append(((estado, nivel), nodo_siguiente))
                nodos.add(nodo_siguiente)
                nuevos.append(nodo_siguiente)

        actuales = nuevos

    return nodos, red


def graficar_red_j1(nodos, aristas, cadena):


    G = nx.DiGraph()

    for nodo in nodos:
        G.add_node(nodo)

    for origen, destino in aristas:
        G.add_edge(origen, destino)

    # Posición por niveles
    pos = {}
    for (estado, nivel) in nodos:
        pos[(estado, nivel)] = (nivel, -estado)

    labels = {(n): f"{n[0]}" for n in nodos}

    plt.figure(figsize=(10,6))

    nx.draw(G, pos, labels=labels, node_size=800, node_color="lightgreen")
    plt.title(f"Árbol de ejecución del NFA\nCadena: {' '.join(cadena)}", fontsize = 20)

    plt.title("Árbol de ejecución del NFA")
    plt.tight_layout()
    plt.show(block=False)
    plt.pause(0.001)

