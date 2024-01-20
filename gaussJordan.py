import numpy as np

class GaussJordanSolver:
    def __init__(self, matrix_size):
        self.matrix_size = matrix_size
        self.A = np.random.rand(matrix_size, matrix_size + 1)  # Rozszerzona macierz (A|b)
        self.x = np.zeros(matrix_size)  # Wektor rozwiązań

    def gauss_jordan_elimination(self):
        for i in range(self.matrix_size):
            # Normalizacja wiersza
            self.A[i, :] /= self.A[i, i]

            # Eliminacja współczynników poniżej i powyżej pivotu
            for j in range(self.matrix_size):
                if i != j:
                    factor = self.A[j, i]
                    self.A[j, :] -= factor * self.A[i, :]

    def solve(self):
        print("Macierz przed eliminacją Gaussa-Jordana:")
        print(self.A)

        self.gauss_jordan_elimination()
        print("\nMacierz po eliminacji Gaussa-Jordana:")
        print(self.A)

        self.x = self.A[:, -1]
        print("\nRozwiązanie:")
        print(self.x)

#solver = GaussJordanSolver(matrix_size)
#solver.solve()
