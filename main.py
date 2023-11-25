#import cholesky
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
                print("dziala")
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