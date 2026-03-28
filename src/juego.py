#------ Para 1 jugador ---------  
def buscar_rutas(
        nfa,
        estado, 
        objetivo, 
        cadena, 
        indice, 
        camino, 
        rutas
    ):

    if indice == len(cadena):

        if estado == objetivo:
            rutas.append(camino.copy())

        return
    
    simbolo = cadena[indice]

    for siguiente in nfa[estado][simbolo]:

        camino.append(siguiente)

        buscar_rutas(
            nfa,
            siguiente,
            objetivo,
            cadena,
            indice + 1,
            camino,
            rutas
        )

        camino.pop()
    

def generar_todas_rutas(nfa, inicio, cadena):

    rutas = []

    buscar_todas_rutas(
        nfa,
        inicio,
        cadena,
        0,
        [inicio],
        rutas
    )

    return rutas


def buscar_todas_rutas(nfa, estado, cadena, indice, camino, rutas):

    if indice == len(cadena):
        rutas.append(camino.copy())
        return

    simbolo = cadena[indice]

    for siguiente in nfa[estado][simbolo]:

        camino.append(siguiente)

        buscar_todas_rutas(
            nfa,
            siguiente,
            cadena,
            indice + 1,
            camino,
            rutas
        )

        camino.pop()


def generar_rutas(nfa, inicio, objetivo, cadena):

    rutas = []

    buscar_rutas(
        nfa, 
        inicio,
        objetivo,
        cadena,
        0,
        [inicio],
        rutas
    )

    return rutas


#--------- Para 2 jugadores -----------

def buscar_rutas_dos_jugadores(
    nfa,
    j1_pos,
    j2_pos,
    turno,
    cadena_j1,
    cadena_j2,
    i1,
    i2,
    camino_j1,
    camino_j2,
    rutas
):
    
    if i1 == len(cadena_j1) and i2 == len(cadena_j2):

        if j1_pos == 16 and j2_pos == 13:
            rutas.append((camino_j1.copy(), camino_j2.copy()))

        return

    #----- Turno del primer jugador -----

    if turno == 1:

        if i1 >= len(cadena_j1):
            buscar_rutas_dos_jugadores(
                nfa, j1_pos, j2_pos, 2,
                cadena_j1, cadena_j2,
                i1, i2,
                camino_j1, camino_j2, rutas
            )
            return

        simbolo = cadena_j1[i1]
        movimientos = nfa[j1_pos][simbolo]

        pudo_mover = False

        for sig in movimientos:

            #---- Bloqueo, no puede caer donde el otro jugador
            if sig == j2_pos:
                continue

            pudo_mover = True

            camino_j1.append(sig)

            buscar_rutas_dos_jugadores(
                nfa,
                sig,
                j2_pos,
                2,  #---- cambia de turno
                cadena_j1,
                cadena_j2,
                i1 + 1,
                i2,
                camino_j1,
                camino_j2,
                rutas
            )

            camino_j1.pop()

        #----- Si no pudo moverse, etnoces va a perder el turno
        if not pudo_mover:
            
            buscar_rutas_dos_jugadores(
                nfa,
                j1_pos,
                j2_pos,
                2,
                cadena_j1,
                cadena_j2,
                i1 + 1,
                i2,
                camino_j1,
                camino_j2,
                rutas
            )
    else:

        if i2 >= len(cadena_j2):
            buscar_rutas_dos_jugadores(
                nfa, j1_pos, j2_pos, 1,
                cadena_j1, cadena_j2,
                i1, i2,
                camino_j1, camino_j2, rutas
            )
            return
        
        simbolo = cadena_j2[i2]
        movimientos = nfa[j2_pos][simbolo]

        pudo_mover = False

        for sig in movimientos:

            if sig == j1_pos:
                continue

            pudo_mover = True

            camino_j2.append(sig)

            buscar_rutas_dos_jugadores(
                nfa,
                j1_pos,
                sig,
                1,
                cadena_j1,
                cadena_j2,
                i1,
                i2 + 1,
                camino_j1,
                camino_j2,
                rutas
            )

            camino_j2.pop()
        
        if not pudo_mover:
            buscar_rutas_dos_jugadores(
                nfa,
                j1_pos,
                j2_pos,
                1,
                cadena_j1,
                cadena_j2,
                i1,
                i2 + 1,
                camino_j1,
                camino_j2,
                rutas
            )


def generar_rutas_dos_jugadores(nfa, cadena_j1, cadena_j2):

    rutas = []

    buscar_rutas_dos_jugadores(
        nfa,
        1,
        4,
        1,
        cadena_j1,
        cadena_j2,
        0,
        0,
        [1],
        [4],
        rutas
    )

    return rutas