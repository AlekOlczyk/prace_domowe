
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


class Uczniowie:
    def __init__(self, imie_ucznia, nazwisko_ucznia, klasa_ucznia, lekcje_ucznia):
        self.imie_ucznia = imie_ucznia
        self.nazwisko_ucznia = nazwisko_ucznia
        self.klasa_ucznia = klasa_ucznia
        self.lekcje_ucznia = lekcje_ucznia

    def __repr__(self):
        return f"Uczeń {self.imie_ucznia} {self.nazwisko_ucznia} z klasy {self.klasa_ucznia}."

class Nauczyciele:
    def __init__(self, imie_nauczyciela, nazwisko_nauczyciela, nazwa_przedmiotu, uczone_klasy, wychowawstwo):
        self.imie_nauczyciela = imie_nauczyciela
        self.nazwisko_nauczyciela = nazwisko_nauczyciela
        self.nazwa_przedmiotu = nazwa_przedmiotu
        self.uczone_klasy = uczone_klasy
        self.wychowawstwo = wychowawstwo

    def __repr__(self):
        return f"Nauczyciel {self.imie_nauczyciela} {self.nazwisko_nauczyciela} prowadzony przedmiot {self.nazwa_przedmiotu} w klasach {self.uczone_klasy}, wychowawca klasy {self.wychowawstwo}."

szkola = {
    "uczniowie": [Uczniowie("Aleksander", "Olczyk", "1b", "polski, geografia"),
                  Uczniowie("Adam", "Malysz", "1a", "geografia, angielski")],
    "nauczyciele": [Nauczyciele("Anna", "Nowak", "polski", "1a", "1a"),
                    Nauczyciele("Ewa", "Swoboda", "geografia", "1b", "1b"),
                    Nauczyciele("Magdalena", "Kowalik", "angielski", "1a, 1b", None)]
          }

def dodanie_ucznia(imie_ucznia, nazwisko_ucznia, klasa_ucznia): # nie działa
    uczniowie.append(imie_ucznia, nazwisko_ucznia, klasa_ucznia)




def wyswielenie_uczniow_i_wychowawcy_w_danej_klasie(klasa_ucznia): #działa
    lista_uczniow = []
    for uczen in szkola.get("uczniowie"):
        if uczen.klasa_ucznia == klasa_ucznia:
            lista_uczniow.append(uczen)
    wychowawca = []
    for nauczyciel in szkola.get("nauczyciele"):
        if nauczyciel.wychowawstwo == klasa_ucznia:
            wychowawca.append(nauczyciel)
    return lista_uczniow, wychowawca

def wyswieltenie_zajec_ucznia_oraz_nauczyciela_prowadzacego(imie_ucznia, nazwisko_ucznia): # nie przypisuje nauczyciela do lekcji
    for uczen in szkola.get("uczniowie"):
        if uczen.imie_ucznia == imie_ucznia and uczen.nazwisko_ucznia == nazwisko_ucznia:
            return uczen.lekcje_ucznia
    for nauczyciel in szkola.get("nauczyciele"):
        if nauczyciel.lekcje_ucznia == nauczyciel.nazwa_przedmiotu:
            return nauczyciel.nazwa_przedmiotu

def wyswietlanie_klas_nauczyciela(imie_nauczyciela, nazwisko_nauczyciela): #działa
    klasy_nauczyciela = []
    for nauczyciel in szkola.get("nauczyciele"):
        if nauczyciel.imie_nauczyciela == imie_nauczyciela and nauczyciel.nazwisko_nauczyciela == nazwisko_nauczyciela:
            klasy_nauczyciela.append(nauczyciel.uczone_klasy)
    return klasy_nauczyciela

# def wyswietlanie_uczniow_wychowawcy(imie_wychowawcy, nazwisko_wychowawcy): #nie działa
#     lista_uczniow_wychowawcy = []
#     for wychowawca in szkola.get("nauczyciele"):
#         if wychowawca.imie_nauczyciela == imie_wychowawcy and wychowawca.nazwisko_nauczyciela == nazwisko_wychowawcy:




while True:
    wybor_uzytkownika = input("Wybierz co chcesz zrobic:\n1. utworz\n2. zarzadzaj\n3. koniec\n")
    if wybor_uzytkownika == "1" or wybor_uzytkownika == "utworz":
        imie_ucznia = input("Podaj imie ucznia, którego chcesz dodać: ")
        nazwisko_ucznia = input("Podaj nazwisko ucznia, którego chcesz dodać: ")
        klasa_ucznia = input("Podaj klase ucznia, którego chcesz dodać: ")

        uczniowie.append(imie_ucznia, nazwisko_ucznia, klasa_ucznia)



    elif wybor_uzytkownika == "2" or wybor_uzytkownika == "zarzadzaj":
        wybor_zarzadzania = input("Wybierz co chcesz zrobic:\n1. klasa\n2. uczen\n3. nauczyciel\n4. wychowawca\n5. koniec\n")
        if wybor_zarzadzania == "1" or wybor_zarzadzania == "klasa":
            wybor_klasy = input("Podaj klase: ")
            uczniowie = wyswielenie_uczniow_i_wychowawcy_w_danej_klasie(wybor_klasy)
            print(uczniowie)

        elif wybor_zarzadzania == "2" or wybor_zarzadzania == "uczen":
            wybor_ucznia_imie = input("Podaj imie ucznia: ")
            wybor_ucznia_nazwisko = input("Podaj nazwisko ucznia: ")
            przedmiot = wyswieltenie_zajec_ucznia_oraz_nauczyciela_prowadzacego(wybor_ucznia_imie, wybor_ucznia_nazwisko)
            print(przedmiot)


        elif wybor_zarzadzania == "3" or wybor_zarzadzania == "nauczyciel":
            wybor_imienia_nauczyciela = input("Podaj imie nauczyciela: ")
            wybor_nazwiska_nauczyciela = input("Podaj nazwisko nauczyciela: ")
            lista_klas = wyswietlanie_klas_nauczyciela(wybor_imienia_nauczyciela, wybor_nazwiska_nauczyciela)
            print(lista_klas)


        elif wybor_zarzadzania == "4" or wybor_zarzadzania == "wychowawca":
            wybor_imienia_wychowawcy = input("Podaj imie wychowawcy: ")
            wybor_nazwiska_wychowawcy = input("Podaj nazwisko wychowawcy: ")
            # lista_uczniow = wyswietlanie_uczniow_wychowawcy(wybor_imienia_wychowawcy, wybor_nazwiska_wychowawcy)
            # print(lista_uczniow)

        elif wybor_zarzadzania == "5" or wybor_zarzadzania == "koniec":
            break

        else:
            print("Błędna komenda!")

    elif wybor_uzytkownika == "3" or wybor_uzytkownika == "zakoncz":
        break
    else:
        print("Błędna komenda!")

