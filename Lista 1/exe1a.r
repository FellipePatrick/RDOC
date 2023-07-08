# Definindo a matriz C
C <- matrix(c(2, 1, -3, 0, 2, 1, 5, 1, 3), nrow = 3, ncol = 3, byrow = TRUE)
print("Matriz C:")
print(C)

# Calculando o determinante
determinante <- det(C)
print("Determinante da matriz C:")
print(determinante)