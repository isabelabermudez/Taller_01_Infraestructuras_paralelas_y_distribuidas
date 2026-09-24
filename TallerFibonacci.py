# TallerFibonacci.py
# Autor: Isabela Bermúdez 2428564
# Descripción: Este código calcula los números de Fibonacci  en paralelo utilizando ThreadPoolExecutor y ProcessPoolExecutor. 
# curso: Infraestructuras Paralelas y Distribuidas

import time 
import concurrent.futures 


#Calculo de fibonacci 
def fibonacci(n): 
    if n <= 1: 
        return n 
    return fibonacci(n - 1) + fibonacci(n - 2) 

## calculo de fibonacci en paralelo
def calcular_fibonacci_paralelo(n_elementos, executor_type): 
    inicio = time.time() 

    with executor_type() as executor:
           futures = [executor.submit(fibonacci, i) for i in range(n_elementos + 1)]
           resultados = [future.result() for future in futures]     ## El for recorre la lista de futures en el orden en que fueron creados, y future.result() espera a que la tarea termine y obtiene el resultado, lo que garantiza que los resultados se guarden en orden.
                                                                   
    fin = time.time() 
    tiempo_ejecucion = fin - inicio 
 
    print(f"Fibonacci ({n_elementos}): {resultados}") 
    print(f"Tiempo de ejecución: {tiempo_ejecucion:.4f} segundos") 

#calculo de fibonacci de manera secuencial
def calcular_fibonacci_secuencial(n_elementos): 
    inicio = time.time() 
    resultados = [fibonacci(i) for i in range(n_elementos + 1)] 
    fin = time.time() 
    tiempo_ejecucion = fin - inicio 
 
    print(f"Fibonacci ({n_elementos}): {resultados}") 
    print(f"Tiempo de ejecución: {tiempo_ejecucion:.4f} segundos")


if __name__ == "__main__":
    print("--- Hilos ---")
    calcular_fibonacci_paralelo(20, concurrent.futures.ThreadPoolExecutor)

    print("--- Procesos ---")
    calcular_fibonacci_paralelo(20, concurrent.futures.ProcessPoolExecutor)

    print("--- Secuencial ---")
    calcular_fibonacci_secuencial(20)




