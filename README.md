# chess-automata
# ♟️ Ajedrez Automata - Simulador de Movimientos

Este proyecto es un simulador de lógica desarrollado para la carrera de **Ingeniería en Sistemas Computacionales (ESCOM - IPN)**. Utiliza conceptos de **Teoría de la Computación** para validar y graficar los movimientos legales de piezas de ajedrez en un tablero reducido de 4x4 mediante el uso de **Autómatas Finitos**.

## Características
- **Lógica de Estados:** Implementación de autómatas para validar transiciones de movimiento.
- **Visualización:** Generación de gráficas de la red de movimientos y el autómata (NFA/DFA).
- **Interacción:** Interfaz de juego básica para probar la legalidad de los movimientos en tiempo real.

## Tecnologías y Librerías
- **Lenguaje:** Python 3.12
- **Gráficos:** Matplotlib / NetworkX (para la visualización de la red y el tablero).
- **Lógica:** Implementación personalizada de la matriz de transición de estados.

## Estructura del Proyecto
- `main.py`: Punto de entrada de la aplicación.
- `automata.py`: Definición de los estados y transiciones del autómata.
- `tablero.py`: Lógica de la cuadrícula 4x4 y posiciones.
- `grafico.py` / `graficar_*.py`: Scripts encargados de la renderización visual de las redes y el NFA.
- `juego.py`: Motor básico para la interacción del usuario.

## Instalación y Uso
1. Clona este repositorio:
   ```bash
   git clone [https://github.com/Diesanzz/chess-automata.git](https://github.com/Diesanzz/chess-automata.git)
