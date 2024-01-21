from gauss import GaussianElimination
from cholesky import Cholesky
from gaussJordan import GaussJordan
from deviation import StandardDeviation
from quadratic import QuadraticEquation
from polynomials import Polynomial
from detrivative import Derivative
from integral import Integral
import numpy as np


def main():
    while True:
        print("Wybierz metodę obliczeniową:")
        print("1. Rozwiązanie układu równań liniowych (metoda eliminacji Gaussa)")
        print("2. Rozwiązanie układu równań liniowych (metoda Cholesky'ego)")
        print("3. Rozwiązanie układu równań liniowych (metoda Gaussa-Jordana)")
        print("4. Obliczenie odchylenia standardowego")
        print("5. Znalezienie miejsc zerowych funkcji kwadratowej")
        print("6. Znalezienie miejsc zerowych wielomianu")
        print("7. Obliczenie pochodnej wielomianu")
        print("8. Obliczenie całki oznaczonej funckji")
        print("9. Obliczenie całki nieoznaczonej funckji")

        choice = input("Twój wybór: ")
        if choice == '1':
            matrix_size = int(input("Podaj rozmiar macierzy:"))
            solver = GaussianElimination(matrix_size)
            solver.solve()
            break

        elif choice == '2':
            matrix_size = int(input("Podaj rozmiar macierzy:"))
            b = np.random.rand(matrix_size)
            solver = Cholesky(matrix_size)
            solver.solve(b)
            break

        elif choice == '3':
            matrix_size = int(input("Podaj rozmiar macierzy:"))
            solver = GaussJordan(matrix_size)
            solver.solve()
            break

        elif choice == '4':
            calculator = StandardDeviation()
            calculator.calculate_and_display_steps()
            break

        elif choice == '5':
            solver = QuadraticEquation()
            solver.solve_quadratic_equation()
            break
        
        elif choice =="6":
            solver = Polynomial()
            solver.solve_and_plot()
            break

        elif choice =="7":
            solver = Derivative()
            solver.solve()
            break
        
        elif choice =="8":
            solver = Integral()
            solver.solve_integral()


        else:
            raise ValueError("Niestety nie znam takiej metody")

if __name__ == "__main__":
    main()
