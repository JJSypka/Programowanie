import cholesky as ch
import 
#import gauss
#import gaussJordan
#import odchylenie
#import quadratic
#import wielomiany

def main():
    print("Z jakiej metody chcesz skorzystac?")
    metoda = input("Metoda: ")
    while True:
        if metoda == "Cholesky":
            macierz = [
                [4, 12, -16],
                [12, 37, -43],
                [-16, -43, 98]]
            cholesky_obliczenia = ch.Cholesky(macierz)
            wynik = ch.Cholesky.display()
            print(wynik)
            break
        elif metoda == "Gauss":
                ...
        elif metoda == "GJordan":
                ...
        elif metoda == "Odchylenie":
                ...
        elif metoda == "Kwadratow":
                ...
        elif metoda == "Wielomiany":
                ...
        else:
            raise ValueError("Niestety nie znam takiej metody!")
    


main()