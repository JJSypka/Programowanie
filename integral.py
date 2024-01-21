import sympy as sp

class Integral:
    def __init__(self):
        self.expression = None
        self.lower_limit = None
        self.upper_limit = None

    def get_user_input(self):
        expression_str = input("Podaj funkcję do całkowania (wyrażenie matematyczne): ")
        self.expression = sp.sympify(expression_str)

        self.lower_limit = float(input("Podaj dolną granicę całkowania: "))
        self.upper_limit = float(input("Podaj górną granicę całkowania: "))

    def calculate_integral(self):
        x = sp.symbols('x')
        integral_value = sp.integrate(self.expression, (x, self.lower_limit, self.upper_limit))
        return integral_value

    def display_steps(self):
        print("\nKroki postępowania:")
        print(f"1. Funkcja do całkowania: {self.expression}")
        print(f"2. Granice całkowania: od {self.lower_limit} do {self.upper_limit}")

    def solve_integral(self):
        self.get_user_input()
        self.display_steps()

        result = self.calculate_integral()
        print(f"\nWynik całkowania: {result}")





