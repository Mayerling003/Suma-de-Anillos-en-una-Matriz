# Suma-de-Anillos-en-una-Matriz
Implementación de un algoritmo para sumar los elementos de un anillo en una matriz cuadrada
# Análisis de Complejidad Algorítmica de la Función sumarAnillo

La función sumarAnillo está diseñada para calcular la suma de los elementos que forman un "anillo" (o borde) de una matriz cuadrada bidimensional. Este anillo corresponde a los elementos ubicados en las posiciones límite de una submatriz definida por el nivel 
𝑘
k dentro de una matriz de tamaño 
𝑑
×
𝑑
d×d.

Descripción del algoritmo
El algoritmo recorre los elementos del anillo en cuatro pasos principales:

*Borde superior: se recorren los elementos desde la posición inicial hasta la posición final de la fila superior del anillo.
*Borde derecho: se recorren los elementos desde la posición superior derecha hacia la posición inferior derecha.
*Borde inferior: se recorren los elementos desde la posición inferior derecha hacia la posición inferior izquierda.
*Borde izquierdo: se recorren los elementos desde la posición inferior izquierda hacia la posición superior izquierda.
En cada iteración, los elementos correspondientes son sumados a una variable acumuladora (suma).

# Complejidad temporal
Para un anillo de tamaño 
𝑛
n, donde 
𝑛
=
fin
−
inicio
+
1
n=fin−inicio+1, los bucles realizan el siguiente número de iteraciones:

*Borde superior: 
𝑛
n iteraciones.
*Borde derecho: 
𝑛
−
1
n−1 iteraciones.
*Borde inferior: 
𝑛
−
1
n−1 iteraciones.
*Borde izquierdo: 
𝑛
−
2
n−2 iteraciones.
*El total de iteraciones realizadas es:

𝑇
(
𝑛
)
=
𝑛
+
(
𝑛
−
1
)
+
(
𝑛
−
1
)
+
(
𝑛
−
2
)
=
4
𝑛
−
4
T(n)=n+(n−1)+(n−1)+(n−2)=4n−4
Por lo tanto, la complejidad temporal es proporcional al tamaño del anillo. Para matrices más grandes, donde 
𝑛
n puede aproximarse a 
𝑑
d (el tamaño total de la matriz), la complejidad temporal se expresa como:

𝑇
(
𝑑
)
=
𝑂
(
𝑑
)
T(d)=O(d)
Esto indica que el tiempo de ejecución crece linealmente con el tamaño del anillo.

Complejidad espacial
La función no requiere estructuras de datos adicionales, ya que trabaja directamente con las posiciones y una variable acumuladora. Por lo tanto, su complejidad espacial es constante:

𝑆
(
𝑑
)
=
𝑂
(
1
)
S(d)=O(1)
Conclusión
El algoritmo sumarAnillo tiene una complejidad temporal lineal, 
𝑂
(
𝑑
)
O(d), adecuada para procesar matrices de gran tamaño de manera eficiente. Su complejidad espacial 
𝑂
(
1
)
O(1) lo convierte en un algoritmo óptimo en términos de uso de memoria, ya que no requiere almacenamiento adicional más allá de las variables utilizadas para el cálculo.
