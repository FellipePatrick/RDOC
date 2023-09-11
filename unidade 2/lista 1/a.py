import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 5, 10)
a = 10
b = 5
y = a * x + b

plt.plot(x, y, label='f(x) = 2x + 3')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Gráfico da Função Afim')
plt.grid(True)
plt.legend()

plt.show()