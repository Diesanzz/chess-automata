import tablero

def construir_nfa():

    transiciones = {}

    for estado in range(1, 17):

        transiciones[estado] = {
            "B": [],
            "N": []
        }
        lista_vecinos = tablero.vecinos(estado)
    

        for v in lista_vecinos:

            color = tablero.color_casilla(v)
            transiciones[estado][color].append(v)

    return transiciones


def imprimir_nfa(nfa):

    for estado in nfa:

        print(f"Estado {estado}")
        print("  B ->", nfa[estado]["B"])
        print("  N ->", nfa[estado]["N"])
        print()


def guardar_nfa(nfa, archivo="nfa.txt"):

    with open(archivo, "w") as f:

        for estado in nfa:

            f.write(f"Estado {estado}\n")
            f.write(f"B -> {nfa[estado]['B']}\n")
            f.write(f"N -> {nfa[estado]['N']}")
            