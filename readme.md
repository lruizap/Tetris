# 🗿 Tetris 🗿

## Descripción

Este es un proyecto de Tetris implementado en Python usando la biblioteca Pygame. Tetris es un juego de rompecabezas clásico en el que el jugador debe manipular piezas de diferentes formas para completar líneas horizontales en una cuadrícula. Cuando se completa una línea, esta desaparece, y las líneas superiores caen para ocupar su lugar. El juego termina cuando las piezas se apilan hasta la parte superior de la cuadrícula.

## Características

- **Movimiento y Rotación de Piezas**: Las piezas pueden moverse hacia la izquierda, derecha y abajo, y rotarse en el sentido de las agujas del reloj.
- **Detección de Colisiones**: El juego detecta colisiones con los bordes de la cuadrícula y otras piezas.
- **Eliminación de Líneas**: Las líneas completas se eliminan y las piezas restantes caen.
- **Interfaz de Usuario**: Una sencilla interfaz gráfica creada con Pygame.

## Requisitos

- **Python 3.x**
- **Pygame**

Puedes instalar Pygame usando pip:

```sh
pip install pygame
```

## Instalación y Ejecución

1. **Clonar el Repositorio**:

   ```sh
   git clone https://github.com/lruizap/tetris.git
   cd tetris
   ```

2. **Ejecutar el Juego**:

   ```sh
   python main.py
   ```

## Controles del Juego

- **Flecha Izquierda**: Mover la pieza a la izquierda
- **Flecha Derecha**: Mover la pieza a la derecha
- **Flecha Abajo**: Mover la pieza hacia abajo
- **Flecha Arriba**: Rotar la pieza

## Estructura del Proyecto

- **main.py**: El archivo principal que inicia el juego y contiene el bucle principal.
- **game_logic.py**: Contiene la lógica del juego, incluyendo el movimiento y la rotación de las piezas, la detección de colisiones y la eliminación de líneas.
- **draw.py**: Contiene las funciones para dibujar la cuadrícula y las piezas en la pantalla.
- **shapes.py**: Define las formas de las piezas y sus colores.

## Contribuciones

Las contribuciones son bienvenidas. Si encuentras algún error o tienes alguna mejora, por favor abre un issue o envía un pull request.

## Créditos

Desarrollado por [lruizap](https://github.com/lruizap).
