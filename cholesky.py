import numpy as np

class CholeskySolver:
    def __init__(self, matrix_size):
        self.matrix_size = matrix_size
        self.A = np.random.rand(matrix_size, matrix_size)
        self.A = np.dot(self.A, self.A.T)  # Zapewniamy, że macierz jest symetryczna i dodatnio określona
        self.L = np.zeros((matrix_size, matrix_size))

    def cholesky_decomposition(self):
        for i in range(self.matrix_size):
            for j in range(i + 1):
                if i == j:
                    self.L[i, i] = np.sqrt(self.A[i, i] - np.sum(self.L[i, :i] ** 2))
                else:
                    self.L[i, j] = (self.A[i, j] - np.sum(self.L[i, :j] * self.L[j, :j])) / self.L[j, j]

    def forward_substitution(self, b):
        y = np.zeros(self.matrix_size)
        for i in range(self.matrix_size):
            y[i] = (b[i] - np.sum(self.L[i, :i] * y[:i])) / self.L[i, i]
        return y

    def backward_substitution(self, y):
        x = np.zeros(self.matrix_size)
        for i in range(self.matrix_size - 1, -1, -1):
            x[i] = (y[i] - np.sum(self.L[i+1:, i] * x[i+1:])) / self.L[i, i]
        return x

    def solve(self, b):
        print("def. Jeżeli macierz A jest rzeczywista, symetryczna i dodatnio określona, to ma ona jedyny rozkład na czynniki A=L⋅L^T, gdzie L jest macierzą trójkątnądolną o dodatnich elementach na głównej przekątnej.")
        self.cholesky_decomposition()
        print("Dekompozycja Cholesky'ego:")
        print(self.L)

        y = self.forward_substitution(b)
        print("\nRozwiązanie po kroku forward substitution:")
        print(y)

        x = self.backward_substitution(y)
        print("\nRozwiązanie końcowe po kroku backward substitution:")
        print(x)

# Przykład użycia
#matrix_size = 3
#b = np.random.rand(matrix_size)  # Losowy wektor b
#solver = CholeskySolver(matrix_size)
#solver.solve(b)
