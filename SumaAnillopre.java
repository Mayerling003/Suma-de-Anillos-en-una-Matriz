package sumaanillo;

import java.util.Random;

public class SumaAnillopre {
    public static void main(String[] args) {
        int inicio = 10;  
        int fin = 100;  
        int incremento = 2; 

        evaluarTiempos(inicio, fin, incremento, 0); 
    }

    public static void evaluarTiempos(int inicio, int fin, int incremento, int anillo) {
        Random rand = new Random();

        System.out.println("Dimension\tAnillo\tTiempo de ejecucion (ms)");
        for (int d = inicio; d <= fin; d += incremento) {
            int[][] matriz = new int[d][d];
            for (int i = 0; i < d; i++) {
                for (int j = 0; j < d; j++) {
                    matriz[i][j] = rand.nextInt(99) + 1;
                }
            }

            long startTime = System.nanoTime();
            int suma = sumarAnillopre(matriz, d, anillo); 
            long endTime = System.nanoTime();

            double tiempoMs = (endTime - startTime) / 1_000_000.0;
            System.out.println(d + "x" + d + "\t" + (anillo + 1) + "\t\t" + tiempoMs);
        }
    }

    public static int sumarAnillopre(int[][] matriz, int d, int k) {
        int suma = 0;
        int inicio = k;
        int fin = d - k - 1;

        /* Borde superior */
        for (int i = inicio; i <= fin; i++) {
            suma += matriz[inicio][i];
        }

        /* Borde derecho */
        for (int i = inicio + 1; i <= fin; i++) {
            suma += matriz[i][fin];
        }

        /* Borde inferior*/
        for (int i = fin - 1; i >= inicio; i--) {
            suma += matriz[fin][i];
        }

        /* Borde izquierdo*/
        for (int i = fin - 1; i > inicio; i--) {
            suma += matriz[i][inicio];
        }

        return suma;
    }
}

