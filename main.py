from gauss import GaussianEliminationSolver
from cholesky import CholeskySolver
from gaussJordan import GaussJordanSolver
from odchylenie import StandardDeviationCalculator
from quadratic import QuadraticEquationSolver
import numpy as np
def main():
    while True:
        print("Wybierz metodę obliczeniową:")
        print("1. Rozwiązanie układu równań liniowych (metoda eliminacji Gaussa)")
        print("2. Rozwiązanie układu równań liniowych (metoda Cholesky'ego)")
        print("3. Rozwiązanie układu równań liniowych (metoda Gaussa-Jordana)")
        print("4. Obliczenie odchylenia standardowego")
        print("5. Znalezienie miejsc zerowych funkcji kwadratowej")

        choice = input("Twój wybór: ")
        if choice == '1':
            matrix_size = int(input("Podaj rozmiar macierzy:"))
            solver = GaussianEliminationSolver(matrix_size)
            solver.solve()
        elif choice == '2':
            matrix_size = int(input("Podaj rozmiar macierzy:"))
            b = np.random.rand(matrix_size)
            solver = CholeskySolver(matrix_size)
            solver.solve(b)
        elif choice == '3':
            matrix_size = int(input("Podaj rozmiar macierzy:"))
            solver = GaussJordanSolver(matrix_size)
            solver.solve()
        elif choice == '4':
            calculator = StandardDeviationCalculator()
            calculator.calculate_and_display_steps()
        elif choice == '5':
            solver = QuadraticEquationSolver()
            solver.solve_quadratic_equation()
        else:
            raise ValueError("Niestety nie znam takiej metody")

if __name__ == "__main__":
    main()
