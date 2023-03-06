# Python-UCR - Projecto 1
**Curso:** Programación con Python Nivel 1.

**Instructor:** Arturo Zamora (I-2023).

**Estudiantes:** 
- Luis Andres Sanchez Núñez.
- John Astúa.



### Esta tarea consta de 6 documentos:

#### Codigo principal del juego - BlackJack Game:

[![Link directo al codigo principal main_blackjack_game.py](https://github.com/SpaceParrot21/Python-UCR/blob/Tarea_5/Tareas/Tarea_5/Final/main_blackjack_game.py)]

#### The following module contains the functions for the following tasks:
- Display menu of users
- Show players' stats
- Show cards
- Show results and 
-Handle game scenarios and save results to 'Stats.txt' file
- Save the results in the player stats file ('Stats.txt')

[![Link directo a codigo main_functions_module.py](https://github.com/SpaceParrot21/Python-UCR/blob/Tarea_5/Tareas/Tarea_5/Final/main_functions_module.py)]

#### Class to create a proper deck of cards containing 52 Card objects (deck)with the help of class_deck.py class to retrun a string in the form “Two of Hearts + unicode value”:

[![Link directo a codigo class_card.py](https://github.com/SpaceParrot21/Python-UCR/blob/Tarea_5/Tareas/Tarea_5/Final/class_card.py)]

#### Contains the values suits, suit values, ranks and the Card Class, we generate a deck of cards, shuffle our deck, and to deal out cards during gameplay:

[![Link directo a codigo class_deck.py](https://github.com/SpaceParrot21/Python-UCR/blob/Tarea_5/Tareas/Tarea_5/Final/class_deck.py)]

#### Hand class may be used to calculate the value of those cards using the values dictionary defined in this file. It also adjusts the value of Aces when appropriate:

[![Link directo a codigo class_hand.py](https://github.com/SpaceParrot21/Python-UCR/blob/Tarea_5/Tareas/Tarea_5/Final/class_hand.py)]

#### This file contains the player stats saved after each game:

[![Link directo a codigo player_stats.txt](https://github.com/SpaceParrot21/Python-UCR/blob/Tarea_5/Tareas/Tarea_5/Final/player_stats.txt)]


**Consideraciones a tomar durante la ejecucion del juego:**

- Para poder jugar necesita tener los 6 documentos de la seccion ***LINK*** en el mismo directorio para poder ejecutar el juego correctamente.
- Solamente un jugador puede juagar a las vez contra el 'dealer'.
- 
- El programa le mostrara un menu de seleccion de usuarios con las siguientes opciones (1. Select an existing user, 2. Create a new user, 3. Start Game, 4. Exit).
-Una vez que ingresa a la opcion selecionada el programa le va a mostrar los valores de acuerdo a la opcion seleccionada.
- El programa cuenta con una lista de Usuarios pre-definida. Sin embargo, el juego le permitira crear un nuevo usuario y sera agregado a la lista de 'Usuarios' pero sera eliminado cuando salga del juego (Asi fue programado el juego). 
- El juego requiere que seleccione un jugador de lo contrario le continuara preguntado que seleccione un usuario.
- Si ingreso un usuario que no esta en la lista el programa le indicara que el usuario no se encuentra registrado.
- El nombre del Usuario con el que desea jugar debe ser ingresado tal y como se lo mostro el programa. De lo contrario se le indicara que el usuario no se encuentra definido.
- El juego le mostrara un mensaje indicandole que el juego ha iniciado el juego luego de que seleciono el usuario y selecciono la opcion 3 para iniciar el juego. A la misma vez, el juego iniciara a barajar la baraja y repartira dos cartas a cada jugador.
- Seguido del paso anterior se le mostra las cartas obtenidas, su total y se le preguntara si desea tomar mas cartas (Hit) o no tomar mas cartas (stand).
- El juego mostrara un mensaje cuando el usuario decida  tomar mas cartas (Hit) y mostrara que el juego esta en progreso cuando el jugador esta tomando mas cartas.
- El juego mostrara un mensaje cuando el usuario decida no tomar mas cartas (stand) y mostrara que el 'Dealer esta jugando.
- El juego constantemente limpiara la terminal/consola eliminando los comandos y resultados ingresados/mostrados. Esta tarea es realizada por medio de una funcion para mantener la terminal/consola limpia para tener una mejor experiencia durante el juego.
- El juego cuenta con un retraso al mostrar ciertos mensajes o al ejecutar las siguiente linea de codigo para agregar suspenso al juego y mejorar la experiencia de juego.
- El juego esta programado para mantener la segunda carta del 'Dealer' escondida hasta que el jugador selecionado decida no tomar mas cartas (stand).
- Una vez concluida una partida el juego mostrara un mensaje indicando si gano o perdio, seguidamente le preguntara si desar jugar de nuevo o salir.
- El programa le mostrara dentro de las opciones la opcion 7 - "SALIR" para salir del programa.

---

### Mejoras a Futuro

- Permitir guardar definitivamente el usuario creado en la lista de 'Usuarios'.
- Mostar el promedio de partidas ganadas y perdidas de un jugador.
- Incluir una opcion en el menu que muestre partidas ganadas y perdidas todos los jugadores.
- Por razones de tiempo la opcion 4 del menu, no termina la ejecucion del juego 

---

### Enunciado

<details>
  <summary>:zap: El juego creado toma en cuenta las siguientes consideraciones:</summary>

<!--START_SECTION:activity-->
1. Permitir jugar una partida completa de blackjack de un jugador contra la
computadora contra la computadora. Para la partida se
utilizará un único mazo (deck) de 52 cartas. 
2. El juego se debe desarrollar en su totalidad en la consola o terminal.
3. La mano de la casa o dealer: se deben desplegar las cartas que tiene la casa, una escondida y las demás abiertas. 
4. Se debe representar las cartas, solamente utilizando los símbolos unicode de
cada palo (bastos, diamantes u oros, flores o cruces y corazones).
5. Mano de cada jugador: mismos requerimientos del punto anterior.
6. Factorial: de 1 número
7. Potencia: 1 número elevado al otro
8. Estado de cada jugador: se debe desplegar si un jugador sigue en
juego, si ganó o perdió.
9. El juego debe tener un menú que permita seleccionar un usuario, inicar nuevo juego, mostrar estadisticas del jugador seleccionado, salir.
10. Cuando se inicia un nuevo juego, la aplicación debe llevar al usuario por todas las etapas del juego. Esto incluye la repartición inicial de cartas, que el o los usuarios (1 o 2) pidan más cartas o paren y que la casa juegue.
11. La casa, al ser manejada por la computadora, debe seguir una lógica
predeterminada, por ejemplo que siempre pida carta si su mano suma menos
de 19.
12. De forma OPCIONAL puede implementar algunas de las manos especiales
del 21 como tres sietes, cinco menores, blackjack, etc. ---> Solamente el BlackJack fue agregado. <---
13. El juego debe almacenar los datos del usuario y las estadísticas en archivos
de texto que serán creados por la aplicación. Usted puede decidir cuántos
archivos de texto crear para lograr los resultados especificados en estos
requerimientos. <Solo un archivo es utilizado> [![Link directo a codigo player_stats.txt](https://github.com/SpaceParrot21/Python-UCR/blob/Tarea_5/Tareas/Tarea_5/Final/player_stats.txt)]
14. El código debe estar organizado en módulos y en clases. Se deben utilizar
los conocimientos adquiridos sobre programación orientada a objetos (OOP).
Usted debe decidir cuáles clases necesita crear para representar los
elementos del juego.
<!--END_SECTION:activity-->


**LINKS:**

[![Link directo al codigo principal codigo_principal_blackjack.py](https://github.com/SpaceParrot21/Python-UCR/blob/Tarea_5/Tareas/Tarea_5/Final/main_blackjack_game.py)]

[![Link directo a codigo main_functions_module.py](https://github.com/SpaceParrot21/Python-UCR/blob/Tarea_5/Tareas/Tarea_5/Final/main_functions_module.py)]

[![Link directo a codigo class_card.py](https://github.com/SpaceParrot21/Python-UCR/blob/Tarea_5/Tareas/Tarea_5/Final/class_card.py)]

[![Link directo a codigo class_deck.py](https://github.com/SpaceParrot21/Python-UCR/blob/Tarea_5/Tareas/Tarea_5/Final/class_deck.py)]

[![Link directo a codigo class_hand.py](https://github.com/SpaceParrot21/Python-UCR/blob/Tarea_5/Tareas/Tarea_5/Final/class_hand.py)]

[![Link directo a codigo player_stats.txt](https://github.com/SpaceParrot21/Python-UCR/blob/Tarea_5/Tareas/Tarea_5/Final/player_stats.txt)]
<br />
<br />

---
