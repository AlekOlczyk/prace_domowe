
# Utwórz program do zarządzania bazą szkolną. Istnieje możliwość tworzenia trzech typów użytkowników (uczeń, nauczyciel, wychowawca) a także zarządzania nimi.
#
# Po uruchomieniu programu można wpisać jedną z następujących komend: utwórz, zarządzaj, koniec.
#
# Polecenie "utwórz" - Przechodzi do procesu tworzenia użytkowników.
# Polecenie "zarządzaj" - Przechodzi do procesu zarządzania użytkownikami.
# Polecenie "koniec" - Kończy działanie aplikacji.
#
# Proces tworzenia użytkowników:
#
# Należy wpisać opcję, którą chcemy wybrać: uczeń, nauczyciel, wychowawca, koniec. Po wykonaniu każdej z opcji (oprócz "koniec") wyświetla to menu ponownie.
# Polecenie "uczeń" - Należy pobrać imię i nazwisko ucznia (jako jedna zmienna, można pobrać je jako dwie zmienne, jeżeli zostanie to poprawnie obsłużone) oraz nazwę klasy (np. "3C")
# Polecenie "nauczyciel" - Należy pobrać imię i nazwisko nauczyciela (jako jedna zmienna, labo dwie, jeżeli zostanie to poprawnie obsłużone), nazwę przedmiotu prowadzonego,
# a następnie w nowych liniach nazwy klas, które prowadzi nauczyciel, aż do otrzymania pustej linii.
# Polecenie "wychowawca" - Należy pobrać imię i nazwisko wychowawcy (jako jedna zmienna, albo dwie, jeżeli zostanie to poprawnie obsłużone), a także nazwę prowadzonej klasy.
# Polecenie "koniec" - Wraca do pierwszego menu.
#
# Proces zarządzania użytkownikami:
#
# Należy wpisać opcję, którą chcemy wybrać: klasa, uczen, nauczyciel, wychowawca, koniec. Po wykonaniu każdej z opcji (oprócz "koniec") wyświetla to menu ponownie.
# Polecenie "klasa" - Należy pobrać klasę, którą chcemy wyświetlić (np. "3C") program ma wypisać wszystkich uczniów, którzy należą do tej klasy, a także wychowawcę tejże klasy.
# Polecenie "uczeń" - Należy pobrać imię i nazwisko uczenia, program ma wypisać wszystkie lekcje, które ma uczeń a także nauczycieli, którzy je prowadzą.
# Polecenie "nauczyciel" - Należy pobrać imię i nazwisko nauczyciela, program ma wypisać wszystkie klasy, które prowadzi nauczyciel.
# Polecenie "wychowawca" - Należy pobrać imię i nazwisko nauczyciela, a program ma wypisać wszystkich uczniów, których prowadzi wychowawca.
# Polecenie "koniec" - Wraca do pierwszego menu.


class Uczniowie: #powinna być lp pojedyczna
    def __init__(self, imie_ucznia, nazwisko_ucznia, klasa_ucznia, lekcje_ucznia=[""]):
        self.imie_ucznia = imie_ucznia
        self.nazwisko_ucznia = nazwisko_ucznia
        self.klasa_ucznia = klasa_ucznia
        self.lekcje_ucznia = lekcje_ucznia

    def __repr__(self):
        return f"Uczeń {self.imie_ucznia} {self.nazwisko_ucznia} z klasy {self.klasa_ucznia}."

    def pokaz_imie_i_nazwisko_ucznia(self):
        return f"{self.imie_ucznia} {self.nazwisko_ucznia}"

    def pokaz_lekcje(self, nauczyciele):
        for przedmiot in self.lekcje_ucznia:
            print(przedmiot)
            for nauczyciel in nauczyciele:
                if nauczyciel.nazwa_przedmiotu == przedmiot:
                    for klasa in nauczyciel.uczone_klasy:
                        if klasa == self.klasa_ucznia:
                            print(nauczyciel.pokaz_imie_i_nazwisko())

    # def pokaz_uczniow(self, nauczyciele):##############
    #     for uczen in self.imie_ucznia and self.nazwisko_ucznia:
    #         print(uczen)
    #         for wychowawca in nauczyciele:
    #             if wychowawca.wychowawstwo == klasa_ucznia:
    #                 print(wychowawca.pokaz_imie_i_nazwisko)


class Nauczyciele: #powinna byc lp pojedyncza
    def __init__(self, imie_nauczyciela, nazwisko_nauczyciela, nazwa_przedmiotu, uczone_klasy, wychowawstwo):
        self.imie_nauczyciela = imie_nauczyciela
        self.nazwisko_nauczyciela = nazwisko_nauczyciela
        self.nazwa_przedmiotu = nazwa_przedmiotu
        self.uczone_klasy = uczone_klasy
        self.wychowawstwo = wychowawstwo

    def __repr__(self):
        return f"Nauczyciel {self.imie_nauczyciela} {self.nazwisko_nauczyciela} prowadzony przedmiot {self.nazwa_przedmiotu} w klasach {self.uczone_klasy}, wychowawca klasy {self.wychowawstwo}."

    def pokaz_imie_i_nazwisko(self):
        return f"{self.imie_nauczyciela} {self.nazwisko_nauczyciela}"

    def pokaz_uczniow_wychowawcy(self, uczniowie):
        for wychowawca in self.wychowawstwo:
            print(f"Wychowawca klasy: {wychowawca}")
            for uczen in uczniowie:
                if uczen.klasa_ucznia == wychowawca:
                    print(uczen.pokaz_imie_i_nazwisko_ucznia())



szkola = {
    "uczniowie": [Uczniowie("Aleksander", "Olczyk", "1b", ["polski", "geografia"]),
                  Uczniowie("Adam", "Malysz", "1a", ["geografia", "angielski"])],
    "nauczyciele": [Nauczyciele("Anna", "Nowak", "polski", ["1a","1b"], ["1a"]),
                    Nauczyciele("Ewa", "Swoboda", "geografia", ["1b","1a"], ["1b"]),
                    Nauczyciele("Magdalena", "Kowalik", "angielski", ["1a", "1b"], ["Brak wychowawstwa"])]
          }



# def wyswielenie_uczniow_i_wychowawcy_w_danej_klasie(klasa_ucznia): #działa
#     lista_uczniow = []
#     for uczen in szkola.get("uczniowie"):
#         if uczen.klasa_ucznia == klasa_ucznia:
#             lista_uczniow.append(uczen)
#     wychowawca = []
#     for nauczyciel in szkola.get("nauczyciele"):
#         if nauczyciel.wychowawstwo == klasa_ucznia:
#             wychowawca.append(nauczyciel)
#     return lista_uczniow, wychowawca


# def wyswieltenie_uczniow_i_wychowawcy_danej_klasy_po_klasie_(klasa_ucznia):###########
#     for uczen in szkola.get("uczniowie"):
#         if uczen.klasa_ucznia == klasa_ucznia:
#             uczen.pokaz_uczniow(szkola["uczniowie"])

def wyswieltenie_uczniow_i_wychowawcy_danej_klasy_po_klasie_(klasa_ucznia):
    uczniowie_klasy = []
    for uczen in szkola.get("uczniowie"):
        if uczen == klasa_ucznia:
            uczniowie_klasy.append(uczen)
    wychowawca_klasy = []
    for wychowawca in szkola.get("nauczyciele"):
        if wychowawca == klasa_ucznia:
            wychowawca_klasy.append(wychowawca)
    return uczniowie_klasy, wychowawca_klasy


def wyswieltenie_zajec_ucznia_oraz_nauczyciela_prowadzacego(imie_ucznia, nazwisko_ucznia):
    for uczen in szkola.get("uczniowie"):
        if uczen.imie_ucznia == imie_ucznia and uczen.nazwisko_ucznia == nazwisko_ucznia:
            uczen.pokaz_lekcje(szkola["nauczyciele"])


def wyswietlanie_klas_nauczyciela(imie_nauczyciela, nazwisko_nauczyciela): #działa
    klasy_nauczyciela = []
    for nauczyciel in szkola.get("nauczyciele"):
        if nauczyciel.imie_nauczyciela == imie_nauczyciela and nauczyciel.nazwisko_nauczyciela == nazwisko_nauczyciela:
            klasy_nauczyciela.append(nauczyciel.uczone_klasy)
    return klasy_nauczyciela


def wyswietlanie_uczniow_wychowawcy(imie_wychowawcy, nazwisko_wychowawcy): #nie działa
    for wychowawca in szkola.get("nauczyciele"):
        if wychowawca.imie_nauczyciela == imie_wychowawcy and wychowawca.nazwisko_nauczyciela == nazwisko_wychowawcy:
            wychowawca.pokaz_uczniow_wychowawcy(szkola["uczniowie"])




while True:
    wybor_uzytkownika = input("Wybierz co chcesz zrobic:\n1. utworz\n2. zarzadzaj\n3. koniec\n")

    if wybor_uzytkownika == "1" or wybor_uzytkownika == "utworz":
        wybor_dodawania = input("Wybierz co chcesz zrobic:\n1. uczen\n2. nauczyciel\n3. wychowawca\n4. koniec\n")

        if wybor_dodawania == "1" or wybor_dodawania == "uczen":
            imie_ucznia = input("Podaj imie ucznia, którego chcesz dodać: ")
            nazwisko_ucznia = input("Podaj nazwisko ucznia, którego chcesz dodać: ")
            klasa_ucznia = input("Podaj klase ucznia, którego chcesz dodać: ")

            nowy_uczen = Uczniowie(imie_ucznia, nazwisko_ucznia, klasa_ucznia, ["angielski"])
            szkola["uczniowie"].append(nowy_uczen)

        elif wybor_dodawania == "2" or wybor_dodawania == "nauczyciel":
            imie_nauczyciela = input("Podaj imie nauczyciela, którego chcesz dodać: ")
            nazwisko_nauczyciela = input("Podaj nazwisko nauczyciela, którego chcesz dodać: ")
            nazwa_przedmiotu = input("Podaj klase ucznia, którego chcesz dodać: ")
            klasy = []
            while True:
                uczone_klasy = input("Podaj klasy, które uczy nauczyciel: ")
                if uczone_klasy == "":
                    break
                klasy.append(uczone_klasy)
            nowy_nauczyciel = Nauczyciele(imie_nauczyciela, nazwisko_nauczyciela, nazwa_przedmiotu, klasy, [None])
            szkola["nauczyciele"].append(nowy_nauczyciel)


        elif wybor_dodawania == "3" or wybor_dodawania == "wychowawca":
            imie_wychowawcy = input("Podaj imie wychowawcy: ")
            nazwisko_wychowawcy = input("Podaj nazwisko wychowawcy: ")
            prowadzona_klasa = input("Podaj nazwe prowadzonej klasy tego nauczyciela: ")

            nowy_wychowawca = Nauczyciele(imie_wychowawcy, nazwisko_wychowawcy,[None], prowadzona_klasa , [None])
            szkola["nauczyciele"].append(nowy_wychowawca)

        elif wybor_dodawania == "4" or wybor_dodawania == "koniec":
            continue

        else:
            print("Błędna komenda")


    elif wybor_uzytkownika == "2" or wybor_uzytkownika == "zarzadzaj":
        wybor_zarzadzania = input("Wybierz co chcesz zrobic:\n1. klasa\n2. uczen\n3. nauczyciel\n4. wychowawca\n5. koniec\n")

        if wybor_zarzadzania == "1" or wybor_zarzadzania == "klasa":
            wybor_klasy = input("Podaj klase: ")
            wynik = wyswieltenie_uczniow_i_wychowawcy_danej_klasy_po_klasie_(wybor_klasy)
            print(wynik)

        elif wybor_zarzadzania == "2" or wybor_zarzadzania == "uczen":
            wybor_ucznia_imie = input("Podaj imie ucznia: ")
            wybor_ucznia_nazwisko = input("Podaj nazwisko ucznia: ")
            wyswieltenie_zajec_ucznia_oraz_nauczyciela_prowadzacego(wybor_ucznia_imie, wybor_ucznia_nazwisko)

        elif wybor_zarzadzania == "3" or wybor_zarzadzania == "nauczyciel":
            wybor_imienia_nauczyciela = input("Podaj imie nauczyciela: ")
            wybor_nazwiska_nauczyciela = input("Podaj nazwisko nauczyciela: ")
            lista_klas = wyswietlanie_klas_nauczyciela(wybor_imienia_nauczyciela, wybor_nazwiska_nauczyciela)
            print(lista_klas)


        elif wybor_zarzadzania == "4" or wybor_zarzadzania == "wychowawca":
            wybor_imienia_wychowawcy = input("Podaj imie wychowawcy: ")
            wybor_nazwiska_wychowawcy = input("Podaj nazwisko wychowawcy: ")
            wyswietlanie_uczniow_wychowawcy(wybor_imienia_wychowawcy, wybor_nazwiska_wychowawcy)

        elif wybor_zarzadzania == "5" or wybor_zarzadzania == "koniec":
            continue

        else:
            print("Błędna komenda!")

    elif wybor_uzytkownika == "3" or wybor_uzytkownika == "zakoncz":
        break
    else:
        print("Błędna komenda!")