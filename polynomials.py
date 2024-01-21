import matplotlib.pyplot as plt
import numpy as np

class Polynomial:
    def __init__(self):
        self.degree = 0
        self.coefficients = []

    def get_user_input(self):
        self.degree = int(input("Podaj stopień wielomianu: "))
        print("Podaj współczynniki wielomianu od najwyższej potęgi do wyrazu wolnego:")

        for i in range(self.degree, -1, -1):
            coeff = float(input(f"Współczynnik przy x^{i}: "))
            self.coefficients.append(coeff)

    def evaluate_polynomial(self, x):
        result = 0
        for i, coeff in enumerate(self.coefficients):
            result += coeff * x**i
        return result

    def calculate_derivative(self):
        derivative_coeffs = [i * coeff for i, coeff in enumerate(self.coefficients)][1:]
        return derivative_coeffs

    def newton_raphson_method(self, initial_guess, tolerance=1e-6, max_iterations=100):
        x0 = initial_guess
        iterations = 0

        while iterations < max_iterations:
            f_x0 = self.evaluate_polynomial(x0)
            f_prime_x0 = self.evaluate_polynomial_derivative(x0)

            if abs(f_prime_x0) < tolerance:
                break

            x1 = x0 - f_x0 / f_prime_x0

            if abs(x1 - x0) < tolerance:
                break

            x0 = x1
            iterations += 1

        return x0

    def solve_polynomial(self):
        self.get_user_input()
        roots = []
        
        for _ in range(self.degree):
            initial_guess = float(input(f"Podaj przybliżoną wartość początkową dla jednego z pierwiastków: "))
            root = self.newton_raphson_method(initial_guess)
            roots.append(root)
            self.coefficients = self.calculate_derivative()

        print("\nPierwiastki wielomianu:")
        for i, root in enumerate(roots, start=1):
            print(f"Pierwiastek {i}: {root}")

    def evaluate_polynomial_derivative(self, x):
        derivative_coeffs = self.calculate_derivative()
        derivative_value = sum([i * coeff * x**(i-1) for i, coeff in enumerate(derivative_coeffs)])
        return derivative_value

    def plot_polynomial(self):
        x_vals = np.linspace(min(roots) - 1, max(roots) + 1, 1000)
        y_vals = [self.evaluate_polynomial(x) for x in x_vals]

        plt.plot(x_vals, y_vals, label="Wielomian")
        plt.axhline(0, color='black', linewidth=0.5)
        plt.axvline(0, color='black', linewidth=0.5)
        plt.scatter(roots, [0] * len(roots), color='red', label="Pierwiastki")
        plt.grid(color='gray', linestyle='--', linewidth=0.5)
        plt.title("Wykres wielomianu")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.legend()
        plt.show()

    def solve_and_plot(self):
        self.solve_polynomial()
        self.plot_polynomial()

