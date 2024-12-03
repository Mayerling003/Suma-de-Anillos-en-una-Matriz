import numpy as np
import matplotlib.pyplot as plt
import timeit

def generar_matriz(d):
    """
    Genera una matriz de dimensiones d x d con valores aleatorios entre 1 y 99.
    """
    return np.random.randint(1, 100, (d, d))

def sumar_anillo(matriz, d, k):
    """
    Calcula la suma de los elementos del anillo k de una matriz d x d.
    """
    suma = 0
    inicio = k
    fin = d - k - 1

    # Borde superior
    for i in range(inicio, fin + 1):
        suma += matriz[inicio][i]

    # Borde derecho
    for i in range(inicio + 1, fin + 1):
        suma += matriz[i][fin]

    # Borde inferior
    for i in range(fin - 1, inicio - 1, -1):
        suma += matriz[fin][i]

    # Borde izquierdo
    for i in range(fin - 1, inicio, -1):
        suma += matriz[i][inicio]

    return suma

def evaluar_tiempos(inicio, fin, incremento, repeticiones=5):
    """
    Evalúa los tiempos de ejecución de la función sumar_anillo para matrices de
    diferentes dimensiones desde 'inicio' hasta 'fin' con un paso de 'incremento'.
    """
    dimensiones = []
    tiempos = []

    for d in range(inicio, fin + 1, incremento):
        matriz = generar_matriz(d)

        # Medir el tiempo promedio de ejecución con múltiples repeticiones
        tiempo = timeit.timeit(lambda: sumar_anillo(matriz, d, 0), number=repeticiones) / repeticiones
        dimensiones.append(d)
        tiempos.append(tiempo * 1000)  # Convertir a milisegundos

    return dimensiones, tiempos

def graficar_tiempos(dimensiones, tiempos):
    """
    Grafica los tiempos de ejecución en función de las dimensiones de las matrices.
    """
    plt.figure(figsize=(12, 7))
    
    # Gráfico principal
    plt.plot(
        dimensiones, tiempos, marker='o', color='#8A2BE2', linestyle='-', linewidth=2, 
        markersize=8, label='Tiempo de ejecución (ms)'
    )
    
    # Diseño mejorado
    plt.title('Tiempos de Ejecución de sumar_anillo', fontsize=18, fontweight='bold', color='midnightblue')
    plt.xlabel('Dimensión de la Matriz (n x n)', fontsize=14, color='black')
    plt.ylabel('Tiempo de Ejecución (ms)', fontsize=14, color='black')
    plt.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.7)
    plt.legend(fontsize=12, loc='upper left')
    
    # Etiquetas en los ejes
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    
    # Mostrar y guardar
    plt.tight_layout()
    plt.savefig("grafico_tiempos_ejecucion.png", dpi=300)
    plt.show()

# Main
if __name__ == "__main__":
    inicio = 10      # Dimensión inicial
    fin = 100        # Dimensión final
    incremento = 10  # Paso entre dimensiones (de 10 en 10)

    dimensiones, tiempos = evaluar_tiempos(inicio, fin, incremento, repeticiones=10)
    graficar_tiempos(dimensiones, tiempos)
