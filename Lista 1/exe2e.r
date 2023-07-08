# Definindo a matriz B
B <- matrix(c(6, 8, 9, -8, -6, 3, 5, 7, -9), nrow = 3, ncol = 3, byrow = TRUE)
print("Matriz B:")
print(B)
# Calculando a adjunta da matriz B
adjunta <- t(solve(B))
print("Adjunta da matriz B:")
print(adjunta)