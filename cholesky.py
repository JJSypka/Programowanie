import numpy as np

class Cholesky:
    def __init__(self, macierz):
        self.macierz = np.array(macierz)
        self.rozmiar = len(macierz)
        self.L = np.zeros((self.rozmiar, self.rozmiar))

    def get_L(self, i, j):
        suma_kwadratow = sum(self.L[i][k] ** 2 for k in range(j))
        if i == j:
            return np.sqrt(self.macierz[i][i] - suma_kwadratow)
        else:
            return (self.macierz[i][j] - suma_kwadratow) / self.L[j][j]

    def cholesky(self):
        for i in range(self.rozmiar):
            for j in range(i+1):
                self.L[i][j] = self.get_L(i, j)

    def display_cholesky():
        cholesky()

        kroki = [
            f'Macierz wejściowa:\n{self.macierz}',
            f'Rozpoczynamy faktoryzację Cholesky\'ego:',
        ]

        for i in range(self.rozmiar):
            for j in range(i + 1):
                kroki.append(f'Obliczamy element L[{i}][{j}]: {self.get_L(i, j)}')
                kroki.append(f'Przypisujemy L[{i}][{j}] = {self.L[i][j]}')

        kroki.append(f'Macierz L (faktoryzacja Cholesky\'ego):\n{self.L}')
        kroki.append(f'Macierz LL^T:\n{np.dot(self.L, self.L.T)}')

        return '\n'.join(kroki)

# Przykład użycia klasy:
macierz = [
    [4, 12, -16],
    [12, 37, -43],
    [-16, -43, 98]
]

#cholesky_obliczenia = Cholesky(macierz)
#wynik = cholesky_display_kroki()
#print(wynik)
