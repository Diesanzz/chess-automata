import pygame
import sys
import time


TAM = 400 
FILAS = 4
CASILLA = TAM // FILAS

BLANCO = (240, 240, 240)
NEGRO = (50, 50, 50)
ROJO = (200, 50, 50)
AZUL = (50, 50, 200)


def estado_a_coord(estado):
    estado -= 1
    fila = estado // 4
    col = estado % 4
    return col * CASILLA, fila * CASILLA


def dibujar_tablero(screen):

    for fila in range(4):
        for col in range(4):

            color = BLANCO if (fila + col) % 2 == 0 else NEGRO

            pygame.draw.rect(
                screen,
                color,
                (col * CASILLA, fila * CASILLA, CASILLA, CASILLA)
            )




def dibujar_piezas(screen, j1, j2):

    x1, y1 = estado_a_coord(j1)
    x2, y2 = estado_a_coord(j2)

    pygame.draw.circle(screen, ROJO, (x1 + CASILLA//2, y1 + CASILLA//2), 20)
    pygame.draw.circle(screen, AZUL, (x2 + CASILLA//2, y2 + CASILLA//2), 20)


def mover_suave(screen, actual, siguiente, otro, es_j1, clock):

    frames = 30

    xi, yi = estado_a_coord(actual)
    xf, yf = estado_a_coord(siguiente)

    xo, yo = estado_a_coord(otro)

    for t in range(frames):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        alpha = t / frames

        x = xi + (xf - xi) * alpha
        y = yi + (yf - yi) * alpha

        screen.fill((0,0,0))
        dibujar_tablero(screen)

        font = pygame.font.SysFont(None, 30)

        turno_texto = "J1" if es_j1 else "J2"
        texto = font.render(f"Turno: {turno_texto}", True, (255,0,255))

        screen.blit(texto, (10, 10))

        # Dibujar el otro fijo
        pygame.draw.circle(screen, AZUL if es_j1 else ROJO,
                           (xo + CASILLA//2, yo + CASILLA//2), 20)

        # Dibujar el que se mueve
        pygame.draw.circle(screen, ROJO if es_j1 else AZUL,
                           (int(x) + CASILLA//2, int(y) + CASILLA//2), 20)

        pygame.display.flip()
        clock.tick(60)


def mostrar_ganador(screen, texto):

    font = pygame.font.SysFont(None, 50)

    if texto == "Gana J1":
        img = font.render(texto, True, (255, 0, 0))
        rect = img.get_rect(center=(TAM//2, TAM//2))  
    elif texto == "Gana J2":
        img = font.render(texto, True, (0, 0, 255))
        rect = img.get_rect(center=(TAM//2, TAM//2))
    else:
        img = font.render(texto, True, (255, 255, 0))
        rect = img.get_rect(center=(TAM//2, TAM//2))


    screen.blit(img, rect)
    pygame.display.flip()


def animar(camino_j1, camino_j2, turno_inicial):

    pygame.init()
    screen = pygame.display.set_mode((TAM, TAM))
    pygame.display.set_caption("Juego 4x4")

    clock = pygame.time.Clock()

    pasos = max(len(camino_j1), len(camino_j2))   

    llego_j1 = None
    llego_j2 = None
    contador_turnos = 0

    while True:

        turno = turno_inicial

        i = 0
        j = 0

        while i < len(camino_j1) - 1 or j < len(camino_j2) - 1:

            if turno == 1 and i < len(camino_j1) - 1:

                siguiente = camino_j1[i+1]

                if siguiente == camino_j2[j]:

                    turno = 2
                    continue

                mover_suave(
                    screen,
                    camino_j1[i],
                    camino_j1[i+1],
                    camino_j2[j],
                    True,
                    clock
                )

                i += 1
                turno = 2
                contador_turnos += 1

                if camino_j1[i] == 16 and llego_j1 is None:
                    llego_j1 = contador_turnos

            elif turno == 2 and j < len(camino_j2) - 1:

                siguiente = camino_j2[j+1]

                if siguiente == camino_j1[i]:
                    turno = 1
                    continue

                mover_suave(
                    screen,
                    camino_j2[j],
                    camino_j2[j+1],
                    camino_j1[i],
                    False,
                    clock
                )

                j += 1
                turno = 1
                contador_turnos += 1

                if camino_j2[j] == 13 and llego_j2 is None:
                    llego_j2 = contador_turnos


            else:
                # Si uno no puede moverse, pierde turno
                turno = 2 if turno == 1 else 1


            if llego_j1 is not None and llego_j2 is not None:

                if llego_j1 < llego_j2:
                    texto = "Gana J1"
                elif llego_j2 < llego_j1:
                    texto = "Gana J2"
                else:
                    texto = "Empate"

            elif llego_j1 is not None:
                texto = "Gana J1"


            elif llego_j2 is not None:
                texto = "Gana J2"

            else:
                texto = "Sin ganador"


            screen.fill((0,0,0))
            dibujar_tablero(screen)
            dibujar_piezas(screen, camino_j1[-1], camino_j2[-1])
            mostrar_ganador(screen, texto)    


        pygame.time.delay(800)