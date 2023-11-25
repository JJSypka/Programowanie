class EliminacjaGaussaJordana:
    def __init__(self, macierz):
        self.macierz = macierz
        self.rozmiar = len(macierz)
        self.wynik = [0] * self.rozmiar

    def display_macierz(self, nazwa, macierz):
        print(f'{nazwa} = ')
        for row in macierz:
            print(row)
        print()

    def display_kroki(self):
        for k in range(self.rozmiar):
            self.display_macierz(f'Krok {k + 1}: Macierz przed eliminacją Gaussa-Jordana', self.macierz)

            # Skalowanie wiersza
            skalar = self.macierz[k][k]
            for j in range(self.rozmiar + 1):
                self.macierz[k][j] /= skalar

            self.display_macierz(f'Krok {k + 1}: Skalowanie wiersza', self.macierz)

            # Eliminacja pozostałych wierszy
            for i in range(self.rozmiar):
                if i != k:
                    wspolczynnik = self.macierz[i][k]

                    for j in range(self.rozmiar + 1):
                        self.macierz[i][j] -= wspolczynnik * self.macierz[k][j]

            self.display_macierz(f'Krok {k + 1}: Eliminacja pozostałych wierszy', self.macierz)

        print('Wyniki:')
        for i in range(self.rozmiar):
            print(f'x{i + 1} = {self.macierz[i][self.rozmiar]}')

# Przykład użycia klasy:
#macierz = [
#    [2, 1, -1, 8],
#    [-3, -1, 2, -11],
#    [-2, 1, 2, -3]

#]

#eliminacja_gaussa_jordana = EliminacjaGaussaJordana(macierz)
#eliminacja_gaussa_jordana.wyswietl_kroki()
