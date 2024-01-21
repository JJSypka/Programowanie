import sympy as sp

class Derivative:
    def __init__(self):
        self.x = sp.symbols('x')
        self.function = None
        self.derivative = None

    def enter_function(self):
        expression = input("Wzór funckji (wykorzystaj zmienna x,a potęgi wprowadz za pomocą '^'): ")
        self.function = sp.sympify(expression)
        self.calculate_derivative()

    def calculate_derivative(self):
        if self.function is not None:
            self.derivative = sp.diff(self.function, self.x)
        else:
            print("Najpierw wprowadz funckje")

    def display_function(self):
        if self.function is not None:
            print(f"Funkcja: {self.function}")
        else:
            print("Najpierw wprowadz funckje!")

    def display_derivative(self):
        if self.derivative is not None:
            print(f"Pochodna: {self.derivative}")
        else:
            print("Najpierw policz pochodna!")

    def solve(self):
        self.enter_function()
        self.calculate_derivative()
        self.display_derivative()

    

