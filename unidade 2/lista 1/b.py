import matplotlib.pyplot as plt
import numpy as np

def funcao_polinomial(x):
    return x**2 - 4*x + 4

x = np.linspace(-5, 5, 100) 

y = funcao_polinomial(x)

plt.plot(x, y, label='f(x) = x^2 - 4x + 4')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Gráfico da Função Polinomial')
plt.grid(True)
plt.legend()

plt.show()

