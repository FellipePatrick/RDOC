import matplotlib.pyplot as plt
import numpy as np

def funcao_modular(x):
    return np.abs(x)

# Criar um array de valores de x no intervalo [-5, 5]
x = np.linspace(-5, 5, 100)  # 100 pontos no intervalo

# Calcular os valores correspondentes de y
y = funcao_modular(x)

# Criar o gráfico
plt.plot(x, y, label='f(x) = |x|')

# Configurar rótulos e legenda
plt.xlabel('x')
plt.ylabel('y')
plt.title('Gráfico da Função Modular')
plt.grid(True)
plt.legend()

# Mostrar o gráfico na tela
plt.show()
