# Definindo a matriz A
A <- matrix(c(2, 6, 7, -5, -6, 3, 5, 4, -2), nrow = 3, ncol = 3, byrow = TRUE)
print("Matriz A:")
print(A)
# Calculando o determinante da matriz inversa de C
detIn <- 1 / det(A)
print("Determinante da matriz inversa de A:")
print(detIn)