from gauss import GaussianEliminationSolver
from cholesky import CholeskySolver
from gaussJordan import GaussJordanSolver
from odchylenie import StandardDeviationCalculator
from quadratic import QuadraticEquationSolver

def main():
    print("Wybierz metodę obliczeniową:")
    print("1. Rozwiązanie układu równań liniowych (metoda eliminacji Gaussa)")
    print("2. Rozwiązanie układu równań liniowych (metoda Cholesky'ego)")
    print("3. Rozwiązanie układu równań liniowych (metoda Gaussa-Jordana)")
    print("4. Obliczenie odchylenia standardowego")
    print("5. Znalezienie miejsc zerowych wielomianu")

    choice = input("Twój wybór: ")

    if choice == '1':
        solver = GaussianEliminationSolver()
        solver.solve()
    elif choice == '2':
        solver = CholeskySolver()
        solver.solve()
    elif choice == '3':
        solver = GaussJordanSolver()
        solver.solve()
    elif choice == '4':
        calculator = StandardDeviationCalculator()
        calculator.calculate_and_display_steps()
    elif choice == '5':
        solver = QuadraticEquationSolver()
        solver.solve_quadratic_equation()
    else:
        print("Nieprawidłowy wybór.")

if __name__ == "__main__":
    main()
