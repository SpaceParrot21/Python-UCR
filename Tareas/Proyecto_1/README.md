# Python-UCR - Projecto 1
**Curso:** Programación con Python Nivel 1.

**Instructor:** Arturo Zamora (I-2023).

**Estudiantes:** 
- Luis Andres Sanchez Núñez.
- John Astúa.



### Esta tarea consta de 6 documentos:

#### - Codigo principal del juego - BlackJack Game:

[![Link directo al codigo principal main_blackjack_game.py](https://github.com/SpaceParrot21/Python-UCR/blob/Tarea_5/Tareas/Tarea_5/Final/main_blackjack_game.py)]

#### - El siguiente módulo contiene las funciones para las siguientes tareas:
- Menú de visualización de los usuarios
- Mostrar las estadísticas de los jugadores
- Mostrar cartas
- Mostrar resultado 
- Manejar escenarios de juego y guardar los resultados en el archivo 'Stats.txt'
- Guardar los resultados en el archivo de estadísticas del jugador ('Stats.txt')

[![Link directo a codigo main_functions_module.py](https://github.com/SpaceParrot21/Python-UCR/blob/Tarea_5/Tareas/Tarea_5/Final/main_functions_module.py)]

#### - Clase para crear un mazo de cartas adecuado que contenga 52 cartas (deck) con la ayuda de la clase class_deck.py para devolver una cadena de la siguiente forma “Two of Hearts + unicode value”:

[![Link directo a codigo class_card.py](https://github.com/SpaceParrot21/Python-UCR/blob/Tarea_5/Tareas/Tarea_5/Final/class_card.py)]

#### - Contiene los valores de los palos, los valores de los palos, los rangos y la clase de la tarjeta, generamos una baraja de cartas, barajamos nuestra baraja, y repartimos cartas durante el juego:

[![Link directo a codigo class_deck.py](https://github.com/SpaceParrot21/Python-UCR/blob/Tarea_5/Tareas/Tarea_5/Final/class_deck.py)]

#### - La clase de mano puede ser utilizada para calcular el valor de esas tarjetas usando los valores del diccionario definido en el file. También ajusta el valor de los ases cuando sea apropiado:

[![Link directo a codigo class_hand.py](https://github.com/SpaceParrot21/Python-UCR/blob/Tarea_5/Tareas/Tarea_5/Final/class_hand.py)]

#### - Este archivo contiene las estadísticas del jugador guardadas después de cada juego y también se utilizará para mostrar las estadísticas del jugador cuando el usuario es seleccionado al inicio del juego:

[![Link directo a codigo player_stats.txt](https://github.com/SpaceParrot21/Python-UCR/blob/Tarea_5/Tareas/Tarea_5/Final/player_stats.txt)]


**Consideraciones a tomar durante la ejecucion del juego:**

- Para poder jugar necesita tener los 6 documentos mencionados en la seccion ***"LINKS"*** en el mismo directorio para poder ejecutar el juego correctamente.
- Solamente un jugador puede juagar a las vez contra el 'dealer'.
- El programa le mostrara un menu de seleccion de usuarios con las siguientes opciones (1. Select an existing user, 2. Create a new user, 3. Start Game, 4. Exit).
- Una vez que ingresa a la opcion selecionada el programa le va a mostrar los valores de acuerdo a la opcion seleccionada.
- El programa cuenta con una lista de Usuarios pre-definida. Sin embargo, el juego le permitira crear un nuevo usuario y sera agregado a la lista de 'Usuarios' pero sera eliminado cuando salga del juego (Asi fue programado el juego). 
- Es un requisito seleccionar un usuario, de lo contrario el progrma continuara preguntado que seleccione un usuario.
- Si ingreso un usuario que no esta en la lista, el programa le indicara que el usuario no se encuentra registrado.
- El nombre del Usuario con el que desea jugar debe ser ingresado tal y como se lo mostro el programa. De lo contrario se le indicara que el usuario no se encuentra definido.
- El programa le mostrara un mensaje indicandole que el juego ha iniciado luego de haber seleccionado el usuario y haber seleccionado la opcion 3. A la misma vez, el juego comenzara a barajar las cartas y repartira dos cartas a cada jugador.
- El juego esta programado para mantener la segunda carta del 'Dealer' escondida hasta que el jugador selecionado decida no tomar mas cartas (stand).
- Seguido del paso anterior se le mostra las cartas obtenidas, su total y se le preguntara si desea tomar mas cartas (Hit) o no tomar mas cartas (stand).
- El juego mostrara un mensaje cuando el usuario decida tomar mas cartas (Hit) y le indicara que el juego esta en progreso cuando el jugador esta tomando mas cartas.
- El juego mostrara un mensaje cuando el usuario decida no tomar mas cartas (stand) y mostrara que el 'Dealer esta jugando.
- El programa constantemente limpiara la terminal/consola eliminando los comandos y resultados ingresados/mostrados. Esta tarea es realizada por medio de una funcion con el fin de obtener una mejor experiencia durante el juego.
- El programa cuenta con pausas variadas durante el juego (sleep()) al mostrar ciertos mensajes o al ejecutar las siguiente linea de codigo, para agregar suspenso y mejorar la experiencia de juego.
- Una vez concluida una partida el juego mostrara un mensaje indicando si gano o perdio, seguidamente le preguntara si desar jugar de nuevo o salir.
- El programa le mostrara dentro de las opciones la opcion 4 - (SALIR) para salir del juego.

---

### Mejoras a Futuro

- Permitir guardar en la lista de 'Usuarios' definitivamente el nuevo usuario creado por el jugador.
- Mostar el promedio de partidas ganadas y perdidas de un jugador.
- Incluir opcion "Estadisticas" en el menu que muestre partidas ganadas y perdidas de todos los jugadores. 

---


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
