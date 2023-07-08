# Definindo a matriz A
A <- matrix(c(2, 6, 7, -5, -6, 3, 5, 4, -2), nrow = 3, ncol = 3, byrow = TRUE)
print("Matriz A:")
print(A)
# Definindo a matriz B
B <- matrix(c(6, 8, 9, -8, -6, 3, 5, 7, -9), nrow = 3, ncol = 3, byrow = TRUE)
print("Matriz B:")
print(B)
# Calculando determinante
determinante <- det(A+B)
print("Determinante de (AB):")
print(determinante)
