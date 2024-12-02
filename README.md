# Tarea 1

Esta operación es sencilla y se puede ejecutar a mano. El resultado se ilustra en la primera sección del código (matriz *Cal9*), junto con el calendario en la forma 5 (matriz *Cal*), la matriz de distancias entre provincias (matriz *DistProv*) y la lista de las subseries de la primera ronda, que determina la distribución Local/Visitador que se empleará durante todo el torneo (matriz *Subseries*). Todos estos datos están proporcionados en el enunciado del problema.

---

# Tarea 2

En esta tarea debemos convertir un calendario dado en cualquier forma (5 o 9) a la otra. Para ello crearemos dos funciones que se encuentran en la segunda sección del código.

- a) La función *C5aC9* convierte un calendario de la forma 5 a la forma 9. Recibe como parámetros un calendario dado en la forma 5, la cantidad de equipos en cuestión y el número de rondas que tiene el campeonato. Por ejemplo, podemos convertir el calendario *Cal* en el calendario *Cal9* ejecutando: C5aC9(Cal,6,3).

- b) La función *C9aC5* convierte un calendario de la forma 9 a la forma 5, recibiendo los mismos parámetros que *C5aC9*, pero en este caso el calendario dado en la forma 9. Por ejemplo, convertimos *Cal9* en el calendario *Cal* ejecutando: C5aC9(Cal,6,3).

La implementación de ambas funciones es muy sencilla, valiéndose cada una de un doble ciclo for.

---

# Tarea 3

Nuevamente crearemos dos funciones, esta vez para calcular las distancias que recorren los equipos en el torneo.

- a) La función *distC9* es la encargada de realizar la tarea en el caso de un calendario expresado en la forma 9. Recibe como parámetros un calendario en la forma 9, la cantidad de equipos que se encuentran compitiendo, el número de rondas que posee el torneo y una matriz de distancias, en este caso *DistProv* pues se trata de Cuba. Devuelve en primer lugar una lista de igual longitud que la cantidad de equipos, donde el elemento *i* representa la distancia total recorrida por el equipo *i*, y seguidamente un número, que será la distancia total recorrida por todos los equipos (en ambos casos en kilómetros).

  Por ejemplo:

|    | 1  | 2  | 3  | 4  | 5  | 6  |
|----|----|----|----|----|----|----|
| 1  | 0  | 1  | 1  | -1 | -1 | -1 |
| 2  | -1 | 0  | 1  | -1 | 1  | 1  |
| 3  | -1 | -1 | 0  | -1 | -1 | 1  |
| 4  | 1  | 1  | 1  | 0  | -1 | -1 |
| 5  | 1  | -1 | 1  | 1  | 0  | -1 |
| 6  | 1  | -1 | -1 | 1  | 1  | 0  |
