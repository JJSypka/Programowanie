class EliminacjaGaussa:
    def __init__(self, macierz):
        self.macierz = macierz
        self.rozmiar = len(macierz)
        self.wynik = [0] * self.rozmiar

    def display_macierz(self, nazwa, macierz):
        print(f'{nazwa} = ')
        for row in macierz:
            print(row)
        print()

    def wyswietl_kroki(self):
        for k in range(self.rozmiar - 1):
            self.display_macierz(f'Krok {k + 1}: Macierz przed eliminacją Gaussa', self.macierz)

            for i in range(k + 1, self.rozmiar):
                wspolczynnik = self.macierz[i][k] / self.macierz[k][k]

                for j in range(k, self.rozmiar + 1):
                    self.macierz[i][j] -= wspolczynnik * self.macierz[k][j]

            self.display_macierz(f'Krok {k + 1}: Macierz po eliminacji Gaussa', self.macierz)

        for i in range(self.rozmiar - 1, -1, -1):
            self.wynik[i] = self.macierz[i][self.rozmiar] / self.macierz[i][i]

            for j in range(i + 1, self.rozmiar):
                self.wynik[i] -= (self.macierz[i][j] / self.macierz[i][i]) * self.wynik[j]

        print('Wyniki:')
        for i in range(self.rozmiar):
            print(f'x{i + 1} = {self.wynik[i]}')

# Przykład użycia klasy:
#macierz = [
#    [2, 1, -1, 8],
#    [-3, -1, 2, -11],
#    [-2, 1, 2, -3]
]

#eliminacja_gaussa = EliminacjaGaussa(macierz)
#eliminacja_gaussa.wyswietl_kroki()
