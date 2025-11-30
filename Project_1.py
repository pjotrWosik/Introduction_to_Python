class Calculator:
    def __init__(self):
        pass
    def dodawanie(self, liczba1, liczba2):
        liczba3 = liczba1 + liczba2
        print(f"wynik dodawania: {liczba1} + {liczba2} = {liczba3}")
    def odejmowanie(self):
        liczba3 = liczba1 - liczba2
        print(f"wynik odejmowania: {liczba1} - {liczba2} = {liczba3}")
    def mnozenie(self):
        pass
    def dzielenie(self):
        pass
    def potegowanie(self):
        pass
    def pierwiastkowanie(self):
        pass
    def historia(self):
        pass
    def wyjscie(self):
        print("program zostaje zamkniety")
    def pobierz_2_liczby(self):
        liczba1 = float(input("podaj 1 liczbe"))
        liczba2 = float(input("podaj 2 liczbe"))
        return liczba1, liczba2


kalk = Calculator()

while True:
    print(":--------------------------------:")
    print("wpisz:")
    print("     1 - dodawanie")
    print("     2 - odejmowanie")
    print("     3 - mnorzenie")
    print("     4 - dzielenie")
    print("     5 - potegowanie")
    print("     6 - pierwiastkowanie")
    print("     7 - Otworz Historie")
    print("     8 - wyjsc z programu")
    print(":--------------------------------:")

    wybur = input("Wybierz dzialanie: ")

    if wybur == "1":
        liczba1, liczba2 = kalk.pobierz_2_liczby()
        kalk.dodawanie(liczba1, liczba2)
    elif wybur == "2":
        liczba1, liczba2 = kalk.pobierz_2_liczby()
        kalk.odejmowanie(liczba1, liczba2)
    elif wybur == "3":
        kalk.mnozenie()
    elif wybur == "4":
        kalk.dzielenie()
    elif wybur == "5":
        kalk.potegowanie()
    elif wybur == "6":
        kalk.pierwiastkowanie()
    elif wybur == "7":
        kalk.historia()
    elif wybur == "8":
        kalk.wyjscie()
        break
