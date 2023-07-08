# Definindo a matriz A e B
A <- matrix(c(2, 6, 7, -5, -6, 3, 5, 4, -2), nrow = 3, ncol = 3, byrow = TRUE)
print("Matriz A:")
print(A)
B <- matrix(c(6, 8, 9, -8, -6, 3, 5, 7, -9), nrow = 3, ncol = 3, byrow = TRUE)
print("Matriz B:")
print(B)
# Calculando o traço de A e B
tracoA <- sum(diag(A))
tracoB <- sum(diag(B))
print("Traco de A:")
print(tracoA)
print("Traco de B:")
print(tracoB)