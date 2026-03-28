import random
from automata import construir_nfa
from juego import generar_rutas_dos_jugadores
from juego import generar_rutas
from juego import generar_todas_rutas
from grafico import animar
from graficar_nfa import graficar_nfa
from graficar_red_j1 import graficar_red_j1
from graficar_red_j1 import construir_red_j1
from graficar_red_j2 import graficar_red_j2
from graficar_red_j2 import construir_red_j2

# ------------------ CONFIG ------------------

LONG_MIN = 3
LONG_MAX = 10

# ------------------ UTILIDADES ------------------

def generar_cadena(longitud):
    return ''.join(random.choice(['B', 'N']) for _ in range(longitud))


def guardar_nfa(nfa):
    with open("nfa.txt", "w") as f:
        for estado in nfa:
            f.write(f"Estado {estado}\n")
            f.write(f"  B -> {nfa[estado]['B']}\n")
            f.write(f"  N -> {nfa[estado]['N']}\n\n")


def guardar_todas_rutas_j1(todas_j1):
    with open("todas_rutas_j1.txt", "w") as f:
        for r in todas_j1:
            f.write(str(r) + "\n")


def guardar_todas_rutas_j2(todas_j2):
    with open("todas_rutas_j2.txt", "w") as f:
        for r in todas_j2:
            f.write(str(r) + "\n")


def guardar_rutas_ganadoras(rutas):
    with open("rutas_ganadoras.txt", "w") as f:
        for r in rutas:
            f.write(str(r) + "\n")


# ------------------ MODO AUTOMATICO ------------------

def modo_automatico(nfa):

    print("\n🔄 Generando cadenas automáticamente...\n")

    while True:

        cadena_j1 = generar_cadena(random.randint(LONG_MIN, LONG_MAX))
        cadena_j2 = generar_cadena(random.randint(LONG_MIN, LONG_MAX))

        rutas = generar_rutas_dos_jugadores(nfa, cadena_j1, cadena_j2)

        if rutas:
            print("✅ Cadenas válidas encontradas")
            print("J1:", cadena_j1)
            print("J2:", cadena_j2)
            return cadena_j1, cadena_j2, rutas

#------------------- VERIFICACIÓN DE CADENA -------


def cadena_valida(cadena):
    return all(c in ['B', 'N'] for c in cadena)


# ------------------ MODO MANUAL ------------------

def modo_manual(nfa):

    print("\n✍️ Modo manual\n")

    # ----------- JUGADOR 1 -----------

    while True:

        cadena_j1 = input("Cadena jugador 1 (N/B)(Termina en B): ").upper()

        if not cadena_valida(cadena_j1):
            print("❌ Solo se permiten caracteres B y N\n")
            continue

        rutas_j1 = generar_rutas(nfa, 1, 16, cadena_j1)

        if rutas_j1:
            print("✅ Cadena válida para J1\n")
            break
        else:
            print("❌ Cadena inválida, intenta de nuevo\n")

    # ----------- JUGADOR 2 -----------

    while True:

        cadena_j2 = input("Cadena jugador 2 (B/N)(Termina en N): ").upper()


        if not cadena_valida(cadena_j2):
            print("❌ Solo se permiten caracteres B y N\n")
            continue


        rutas_j2 = generar_rutas(nfa, 4, 13, cadena_j2)

        if rutas_j2:
            print("✅ Cadena válida para J2\n")
            break
        else:
            print("❌ Cadena inválida, intenta de nuevo\n")

    # ----------- VALIDACION CONJUNTA -----------

    rutas = generar_rutas_dos_jugadores(nfa, cadena_j1, cadena_j2)

    if not rutas:
        print("⚠️ Las cadenas son válidas individualmente pero no funcionan juntas")
        return modo_manual(nfa)  # 🔁 vuelve a pedir todo

    return cadena_j1, cadena_j2, rutas


# ------------------ MAIN ------------------

def main():

    print("===== JUEGO AUTÓMATA 4x4 =====")

    nfa = construir_nfa()
    guardar_nfa(nfa)

    graficar_nfa(nfa)

    print("\n1. Modo automático")
    print("2. Modo manual")

    opcion = input("Seleccione opción: ")

    if opcion == "1":
        cadena_j1, cadena_j2, rutas = modo_automatico(nfa)

    elif opcion == "2":
        cadena_j1, cadena_j2, rutas = modo_manual(nfa)

        if rutas is None:
            return

    else:
        print("Opción inválida")
        return

    # ------------------ TURNO ALEATORIO ------------------

    turno_inicial = random.choice([1, 2])
    print(f"\n🎲 Inicia el jugador {turno_inicial}")

    # ------------------ GUARDAR RUTAS ------------------

    todas_j1 = generar_todas_rutas(nfa, 1, cadena_j1)
    todas_j2 = generar_todas_rutas(nfa, 4, cadena_j2)
    guardar_todas_rutas_j1(todas_j1)
    guardar_todas_rutas_j2(todas_j2)
    guardar_rutas_ganadoras(rutas)

    #------------------- GRAFICAR REDES --------------------
    nodos_j1, aristas_j1 = construir_red_j1(nfa, 1, cadena_j1)
    graficar_red_j1(nodos_j1, aristas_j1, cadena_j1)

    nodos_j2, aristas_j2 = construir_red_j2(nfa, 4, cadena_j2)
    graficar_red_j2(nodos_j2, aristas_j2, cadena_j2)

    # ------------------ EJECUTAR ANIMACION ------------------

    camino_j1, camino_j2 = rutas[0]

    print("\n🎮 Iniciando animación...")

    animar(camino_j1, camino_j2, turno_inicial)


# ------------------ RUN ------------------

if __name__ == "__main__":
    main()
