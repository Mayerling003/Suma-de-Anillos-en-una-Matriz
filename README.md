# Suma de Anillos en una Matriz
Implementación de un algoritmo para sumar los elementos de un anillo en una matriz cuadrada.

## Análisis de Complejidad Algorítmica de la Función `sumarAnillo`

La función `sumarAnillo` está diseñada para calcular la suma de los elementos que forman un "anillo" (o borde) de una matriz cuadrada bidimensional. Este anillo corresponde a los elementos ubicados en las posiciones límite de una submatriz definida por el nivel `k` dentro de una matriz de tamaño `d × d`.

### Descripción del Algoritmo
El algoritmo recorre los elementos del anillo en cuatro pasos principales:

1. **Borde superior**: Se recorren los elementos desde la posición inicial hasta la posición final de la fila superior del anillo.
2. **Borde derecho**: Se recorren los elementos desde la posición superior derecha hacia la posición inferior derecha.
3. **Borde inferior**: Se recorren los elementos desde la posición inferior derecha hacia la posición inferior izquierda.
4. **Borde izquierdo**: Se recorren los elementos desde la posición inferior izquierda hacia la posición superior izquierda.

En cada iteración, los elementos correspondientes son sumados a una variable acumuladora (`suma`).

---

## Complejidad Temporal
Para un anillo de tamaño `n`, donde `n = fin − inicio + 1`, los bucles realizan el siguiente número de iteraciones:

- **Borde superior**: `n` iteraciones.
- **Borde derecho**: `n − 1` iteraciones.
- **Borde inferior**: `n − 1` iteraciones.
- **Borde izquierdo**: `n − 2` iteraciones.

El total de iteraciones realizadas es:

```markdown
T(n) = n + (n − 1) + (n − 1) + (n − 2) = 4n − 4

Por lo tanto, la complejidad temporal es proporcional al tamaño del anillo. Para matrices más grandes, donde n puede aproximarse a d (el tamaño total de la matriz), la complejidad temporal se expresa como:
T(d) = O(d)
# Complejidad espacial
S(d) = O(1)
Conclusión
El algoritmo sumarAnillo tiene una complejidad temporal lineal, O(d), adecuada para procesar matrices de gran tamaño de manera eficiente. Su complejidad espacial O(1) lo convierte en un algoritmo óptimo en términos de uso de memoria, ya que no requiere almacenamiento adicional más allá de las variables utilizadas para el cálculo.


