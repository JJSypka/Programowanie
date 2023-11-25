class Wielomiany:
    def __init__(self, wspolczynniki, epsilon=1e-6, max_iter=100):
        self.wspolczynniki = wspolczynniki
        self.stopien = len(wspolczynniki) - 1
        self.epsilon = epsilon
        self.max_iter = max_iter

    def oblicz_wartosc(self, x):
        return sum(coef * x**i for i, coef in enumerate(self.wspolczynniki))

    def oblicz_pochodna(self, x):
        return sum(i * coef * x**(i-1) for i, coef in enumerate(self.wspolczynniki) if i > 0)

    def znajdz_miejsce_zerowe(self, x0=0.0):
        x = x0
        iteracja = 0

        while True:
            iteracja += 1
            f_x = self.oblicz_wartosc(x)
            f_prime_x = self.oblicz_pochodna(x)

            if abs(f_x) < self.epsilon or iteracja >= self.max_iter:
                break

            # Metoda Newtona-Raphsona do znajdowania miejsca zerowego
            x = x - f_x / f_prime_x

        if abs(f_x) < self.epsilon:
            return f'Miejsce zerowe wielomianu znalezione: x = {x} po {iteracja} iteracjach'
        else:
            return 'Nie udało się znaleźć miejsca zerowego w zadanej liczbie iteracji'

    def wyswietl_kroki(self, x0=0.0):
        kroki = [
            f'Szukamy miejsca zerowego wielomianu stopnia {self.stopien}',
            f'Rozpoczynamy od punktu x = {x0}',
            f'Wielomian: {" + ".join(f"{coef}x^{i}" for i, coef in enumerate(self.wspolczynniki))} = 0'
        ]

        miejsce_zerowe = self.znajdz_miejsce_zerowe(x0)
        kroki.append(miejsce_zerowe)

        return '\n'.join(kroki)

# Przykład użycia klasy:
wspolczynniki = [1, -6, 11, -6]  # Przykładowy wielomian x^3 - 6x^2 + 11x - 6
miejsca_zerowe_obliczenia = Wielomiany(wspolczynniki)
wynik = miejsca_zerowe_obliczenia.wyswietl_kroki()
print(wynik)
