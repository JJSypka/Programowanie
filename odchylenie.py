import math

class OdchylenieStandardowe:
    def __init__(self, dane):
        self.dane = dane

    def mean(self):
        return sum(self.dane) / len(self.dane)

    def oblicz_kwadraty_odchylen(self, srednia):
        return [(x - srednia) ** 2 for x in self.dane]

    def oblicz_odchylenie_standardowe(self):
        srednia = self.mean()
        kwadraty_odchylen = self.oblicz_kwadraty_odchylen(srednia)
        srednia_kwadratow = sum(kwadraty_odchylen) / len(self.dane)
        odchylenie_standardowe = math.sqrt(srednia_kwadratow)
        return odchylenie_standardowe

    def wyswietl_kroki(self):
        srednia = self.mean()
        kwadraty_odchylen = self.oblicz_kwadraty_odchylen(srednia)
        srednia_kwadratow = sum(kwadraty_odchylen) / len(self.dane)
        odchylenie_standardowe = math.sqrt(srednia_kwadratow)

        kroki = [
            f'Dane: {self.dane}',
            f'Średnia: {srednia}',
            f'Kwadraty odchyleń od średniej: {kwadraty_odchylen}',
            f'Średnia kwadratów odchyleń: {srednia_kwadratow}',
            f'Odchylenie standardowe: {odchylenie_standardowe}'
        ]

        return '\n'.join(kroki)

# Przykład użycia klasy:
#dane = [2, 4, 4, 4, 5, 5, 7, 9]
#odchylenie_standardowe_obliczenia = OdchylenieStandardowe(dane)
#wynik = odchylenie_standardowe_obliczenia.wyswietl_kroki()
#print(wynik)
