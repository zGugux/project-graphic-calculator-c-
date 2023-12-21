#Gustavo Rocha de Barros
#DRE: 119050063
#Avaliação Final


#Imports
import numpy as np
import matplotlib.pyplot as plt

#Funcoes
def polinomio (x, coeficientes):
    grau = len(coeficientes) - 1
    resultado = sum(coeficientes[i] * (x ** (grau - i)) for i in range(grau +1))
    return resultado


def plotar_polinomio(coeficientes):

    x_valores = np.linspace (-10, 10, 1000)

    y_valores = [polinomio(x, coeficientes) for x in x_valores]

    plt.plot(x_valores, y_valores, label='Polinomio')

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Gráfico do Polinomio')


    plt.legend()
    plt.grid(true)
    plt.show()


coeficientes = []
 plotar_polinomio(coeficientes) 