import matplotlib.pyplot as plt
import numpy as np

# Criar um array de valores de x no intervalo [0, 2π] para um ciclo completo
x = np.linspace(0, 2 * np.pi, 100)  # 100 pontos no intervalo

# Calcular os valores correspondentes de seno e cosseno
y_seno = np.sin(x)
y_cosseno = np.cos(x)

# Criar o gráfico para o seno
plt.plot(x, y_seno, label='Seno(x)', color='blue')

# Criar o gráfico para o cosseno
plt.plot(x, y_cosseno, label='Cosseno(x)', color='red')

# Configurar rótulos e legenda
plt.xlabel('x')
plt.ylabel('y')
plt.title('Gráfico das Funções Seno e Cosseno')
plt.grid(True)
plt.legend()

# Mostrar o gráfico na tela
plt.show()
