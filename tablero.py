SIZE = 4


DIRECCIONES = [
    (-1,-1), (-1,0), (-1,1), 
    (0,-1),          (0,1),
    (1,-1),   (1,0), (1,1)
]


def pos_to_coord(pos):

    pos -= 1
    fila = pos // SIZE
    columna = pos % SIZE
    return fila, columna


def coord_to_pos(fila, columna):

    return fila * SIZE + columna + 1


def color_casilla(pos):

    fila, columna = pos_to_coord(pos)

    if(fila + columna) % 2 == 0:
        return "B"
    else:
        return "N"
    

def vecinos(pos):

    fila, columna = pos_to_coord(pos)

    lista_vecinos = []

    for df, dc in DIRECCIONES:
        nf = fila + df
        nc = columna + dc

        if 0 <= nf < SIZE and 0 <= nc < SIZE:
            lista_vecinos.append(coord_to_pos(nf, nc))

    return lista_vecinos


def imprimir_tablero():

    for fila in range(SIZE):

        linea = ""

        for col in range(SIZE):

            pos = coord_to_pos(fila, col)
            color = color_casilla(pos)

            linea += f"{pos:2}{color} "
            
        print(linea)
    
    print()
        

