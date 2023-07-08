# Definindo a matriz A
A <- matrix(c(2, 6, 7, -5, -6, 3, 5, 4, -2), nrow = 3, ncol = 3, byrow = TRUE)
print("Matriz A:")
print(A)
# Calculando a adjunta da matriz A
adjunta <- t(solve(A))
print("Adjunta da matriz A:")
print(adjunta)