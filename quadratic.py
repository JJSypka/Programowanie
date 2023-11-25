import math

class QuadraticEquation:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def find_delta(self):
        self.delta = self.b**2 - 4 * self.a * self.c
        return self.delta

    def solve_equation(self):
        delta = self.find_delta()

        if delta > 0:
            x1 = (-self.b + math.sqrt(delta)) / (2 * self.a)
            x2 = (-self.b - math.sqrt(delta)) / (2 * self.a)
            return f'Dwa pierwiastki rzeczywiste: x1 = {x1}, x2 = {x2}'
        elif delta == 0:
            x = -self.b / (2 * self.a)
            return f'Jeden pierwiastek rzeczywisty: x = {x}'
        else:
            # Dla delty mniejszej od zera równanie kwadratowe nie ma pierwiastków rzeczywistych
            # W tym przypadku możemy wykorzystać pierwiastki zespolone
            pierwiastek_delta = math.sqrt(abs(delta)) * 1j
            x1 = (-self.b + pierwiastek_delta) / (2 * self.a)
            x2 = (-self.b - pierwiastek_delta) / (2 * self.a)
            return f'Dwa pierwiastki zespolone: x1 = {x1}, x2 = {x2}'

    def display(self):
        delta = self.find_delta()

        kroki = [
            f'Równanie kwadratowe: {self.a}x^2 + {self.b}x + {self.c} = 0',
            f'Delta: delta = {self.b}^2 - 4 * {self.a} * {self.c} = {delta}'
        ]

        if delta > 0:
            kroki.append(f'Delta > 0. Równanie ma dwa pierwiastki rzeczywiste.')
            kroki.append(self.solve_equation())
        elif delta == 0:
            kroki.append(f'Delta = 0. Równanie ma jeden pierwiastek rzeczywisty.')
            kroki.append(self.solve_equation())
        else:
            kroki.append(f'Delta < 0. Równanie ma dwa pierwiastki zespolone.')
            kroki.append(self.solve_equation())

        return '\n'.join(kroki)




#rownanie = QuadraticEquation(1, -3, 2)
#wynik = rownanie.display()
#print(wynik)
