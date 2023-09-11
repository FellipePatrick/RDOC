import matplotlib.pyplot as plt
import numpy as np

def funcao_quadratica(x):
    return x**2 - 4*x + 4

# Criar um array de valores de x no intervalo [-5, 5]
x = np.linspace(-5, 5, 100)  # 100 pontos no intervalo

y = funcao_quadratica(x)

plt.plot(x, y, label='f(x) = x^2 - 4x + 4')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Gráfico da Função Quadrática')
plt.grid(True)
plt.legend()
plt.show()
