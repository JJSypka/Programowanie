import numpy as np

class GaussianEliminationSolver:
    def __init__(self, matrix_size):
        self.matrix_size = matrix_size
        self.A = np.random.rand(matrix_size, matrix_size + 1)  # Rozszerzona macierz (A|b)
        self.x = np.zeros(matrix_size)  # Wektor rozwiązań

    def gaussian_elimination(self):
        for i in range(self.matrix_size):
            # Wybór elementu głównego (pivot)
            pivot_index = np.argmax(np.abs(self.A[i:, i])) + i
            self.A[[i, pivot_index], :] = self.A[[pivot_index, i], :]

            # Eliminacja współczynników poniżej pivotu
            for j in range(i + 1, self.matrix_size):
                factor = self.A[j, i] / self.A[i, i]
                self.A[j, i:] -= factor * self.A[i, i:]

    def back_substitution(self):
        for i in range(self.matrix_size - 1, -1, -1):
            self.x[i] = (self.A[i, -1] - np.dot(self.A[i, i+1:-1], self.x[i+1:])) / self.A[i, i]

    def solve(self):
        print("Macierz przed eliminacją Gaussa:")
        print(self.A)

        self.gaussian_elimination()
        print("\nMacierz po eliminacji Gaussa:")
        print(self.A)

        self.back_substitution()
        print(f"\nRozwiązanie po wyliczeniu {matrix_size} niewiadomych z macierzy schodkowej:")
        print(self.x)

# Przykład użycia
matrix_size = 3
#solver = GaussianEliminationSolver(matrix_size)
#solver.solve()
