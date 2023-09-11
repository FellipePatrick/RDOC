import matplotlib.pyplot as plt
import numpy as np

def funcao_logaritmica(x):
    return np.log(x)

# Criar um array de valores de x no intervalo [1, 5]
x = np.linspace(-5, 5, 100)  # 100 pontos no intervalo

# Calcular os valores correspondentes de y
y = funcao_logaritmica(x)

# Criar o gráfico
plt.plot(x, y, label='f(x) = log(x)')

# Configurar rótulos e legenda
plt.xlabel('x')
plt.ylabel('y')
plt.title('Gráfico da Função Logarítmica')
plt.grid(True)
plt.legend()

# Mostrar o gráfico na tela
plt.show()