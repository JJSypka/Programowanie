import math

class StandardDeviationCalculator:
    def __init__(self):
        self.data = []

    def get_user_input(self):
        n = int(input("Podaj liczbę danych: "))
        print("Wprowadź wartości:")
        for i in range(n):
            value = float(input(f"Dane {i + 1}: "))
            self.data.append(value)

    def calculate_mean(self):
        mean = sum(self.data) / len(self.data)
        return mean

    def calculate_standard_deviation(self):
        mean = self.calculate_mean()

        # Obliczanie kwadratu różnicy między każdym elementem a średnią
        squared_diff = [(x - mean)**2 for x in self.data]

        # Obliczanie średniej arytmetycznej kwadratów różnic
        mean_squared_diff = sum(squared_diff) / len(self.data)

        # Obliczanie pierwiastka kwadratowego z średniej arytmetycznej kwadratów różnic
        standard_deviation = math.sqrt(mean_squared_diff)

        return standard_deviation

    def calculate_and_display_steps(self):
        self.get_user_input()
        mean = self.calculate_mean()
        print(f"\nŚrednia: {mean}")

        standard_deviation = self.calculate_standard_deviation()
        print(f"\nOdchylenie standardowe: {standard_deviation}")


#calculator = StandardDeviationCalculator()
#calculator.calculate_and_display_steps()
