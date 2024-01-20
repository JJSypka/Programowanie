import matplotlib.pyplot as plt
import numpy as np

class QuadraticEquationSolver:
    def __init__(self):
        self.coefficients = []

    def get_user_input(self):
        print("Podaj współczynniki funkcji kwadratowej ax^2 + bx + c:")
        a = float(input("a: "))
        b = float(input("b: "))
        c = float(input("c: "))
        self.coefficients = [a, b, c]

    def calculate_discriminant(self):
        a, b, c = self.coefficients
        discriminant = b**2 - 4 * a * c
        return discriminant

    def calculate_roots(self):
        a, b, c = self.coefficients
        discriminant = self.calculate_discriminant()

        if discriminant > 0:
            root1 = (-b + np.sqrt(discriminant)) / (2 * a)
            root2 = (-b - np.sqrt(discriminant)) / (2 * a)
            return root1, root2
        elif discriminant == 0:
            root = -b / (2 * a)
            return root,
        else:
            return None  # Brak rzeczywistych miejsc zerowych

    def display_steps(self):
        roots = self.calculate_roots()
        if roots is not None:
            print("\nMiejsca zerowe funkcji kwadratowej:")
            for i, root in enumerate(roots, start=1):
                print(f"Miejsce zero {i}: {root}")
        else:
            print("\nBrak rzeczywistych miejsc zerowych.")

    def plot_function(self):
        a, b, c = self.coefficients
        x = np.linspace(-10, 10, 100)
        y = a * x**2 + b * x + c

        plt.plot(x, y, label=f'{a}x^2 + {b}x + {c}')
        plt.axhline(0, color='black',linewidth=0.5)
        plt.axvline(0, color='black',linewidth=0.5)
        plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
        plt.title("Wykres funkcji kwadratowej")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.legend()
        plt.show()

    def calculate_vertex(self):
        a, b, c = self.coefficients
        x_vertex = -b / (2 * a)
        y_vertex = a * x_vertex**2 + b * x_vertex + c
        print(f"Wierzchołek znajduje się w punkcie {x_vertex}, {y_vertex}")
    
    def solve_quadratic_equation(self):
        self.get_user_input()
        self.display_steps()
        self.calculate_vertex()
        self.plot_function()


#solver = QuadraticEquationSolver()
#solver.solve_quadratic_equation()
