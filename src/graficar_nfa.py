import networkx as nx
import matplotlib.pyplot as plt

def graficar_nfa(nfa):

    G = nx.DiGraph()

    # ---- Agregar nodos ----
    for estado in nfa:
        G.add_node(estado)

    # ---- Agregar aristas ----
    for estado in nfa:
        for simbolo in ['B', 'N']:
            for destino in nfa[estado][simbolo]:
                G.add_edge(estado, destino, label=simbolo)

    # ---- Posiciones (cuadrícula 4x4) ----
    pos = {}
    for estado in nfa:
        fila = (estado - 1) // 4
        col = (estado - 1) % 4
        pos[estado] = (col, -fila)  # invertimos Y para que se vea como tablero

    # ---- Dibujar ----
    plt.figure(figsize=(6,6))

    nx.draw(
        G, pos,
        with_labels=True,
        node_size=800,
        node_color="lightblue",
        font_weight="bold"
    )

    # ---- Etiquetas de aristas ----
    edge_labels = nx.get_edge_attributes(G, 'label')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    plt.title("Autómata NFA del tablero 4x4")
    plt.show()
