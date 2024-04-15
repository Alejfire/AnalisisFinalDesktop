import numpy as np
import matplotlib.pyplot as plt

def resolverSistema(coeficientes, constantes):
    try:
        solution = np.linalg.solve(coeficientes, constantes)
        return list(solution)
    except np.linalg.LinAlgError:
        return None 

def organizarSoluciones(soluciones, numVariables, ascending=True):
    if soluciones is None:
        return []  

    if numVariables == 2:
        return sorted(soluciones) if ascending else sorted(soluciones, reverse=True)
    elif numVariables == 3:
        return sorted(soluciones, reverse=not ascending)

def estaResuelto(soluciones):
    return soluciones is not None and len(set(soluciones)) == 1

def factorialIterativo(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def factorialRecursivo(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorialRecursivo(n - 1)
    
def graficarEcuaciones(coeficientes, constantes, colors = None):
    x = np.linspace(-10, 10, 400)
    plt.figure(figsize=(8, 6))

    for i in range(len(coeficientes)):
        coef = coeficientes[i]
        const = constantes[i]
        color = colors[i] if colors else None
        if coef[1] != 0:
            m = -coef[0] / coef[1]
            b = const / coef[1]
            y = m * x + b
            plt.plot(x, y, label=f"Ecuacion {i+1}: y = {m:.2f}x + {b:.2f}", color = color)
        else:
            plt.axvline(x=const / coef[0], linestyle='--', label=f"Ecuacion {i+1}: x = {const / coef[0]:.2f}", color = color)

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Grafico de las ecuaciones lineales')
    plt.grid(True)
    plt.legend()
    plt.show()

def recibirInput(numEcuaciones, numVariables):
    coeficientes = []
    constantes = []
    
    for i in range(numEcuaciones):
        print(f"Ingrese los coeficientes de la ecuacion {i+1}:")
        coef = []
        for j in range(numVariables):
            value = float(input(f"Coeficiente {j+1}: "))
            coef.append(value)
        coeficientes.append(coef)
        
        constant = float(input(f"Ingrese el termino independiente de la ecuacion {i+1}: "))
        constantes.append(constant)
    
    return np.array(coeficientes), np.array(constantes)

numEcuaciones = 2
numVariables = 2
coeficientes_2var, constantes_2var = recibirInput(numEcuaciones, numVariables)

solution_2var = resolverSistema(coeficientes_2var, constantes_2var)
print("Solucion del sistema de 2 variables:", solution_2var)

colors = ['red', 'blue']

graficarEcuaciones(coeficientes_2var, constantes_2var, colors)