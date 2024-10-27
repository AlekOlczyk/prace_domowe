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

uczniowie = [{
    "imie": "Adam",
    "nazwisko": "Malysz",
    "klasa": "1b",
    "lekcje": ["polski", "geografia"]
    },
    {
    "imie": "Tomasz",
    "nazwisko": "Adamczyk",
    "klasa": "3a",
    "lekcje": ["geografia", "polski"]
    }
]
nauczyciele = [{
    "imie": "Monika",
    "nazwisko": "Polska",
    "nazwa_przedmiotu": "polski",
    "prowadzone_klasy": "1a, 1b, 1c"
    },
    {
    "imie": "Iwona",
    "nazwisko": "Kowalik",
    "nazwa_przedmiotu": "geografia",
    "prowadzona_klasy": "2a, 1b, 3a"
    }
]
wychowawca = [{
    "imie": "Ewa",
    "nazwisko": "Swoboda",
    "wychowawstwo": "1b"
    },
    {
    "imie": "Marek",
    "nazwisko": "Polski",
    "wychowawstwo": "3a"
    }
]

def tworzenie_ucznia():
    imie_ucznia = input("Podaj imie ucznia, którego chcesz dodać: ")
    nazwisko_ucznia = input("Podaj nazwisko ucznia, którego chcesz dodać: ")
    klasa_ucznia = input("Podaj klasę, w której jest uczeń: ")

    nowy_uczen = [{
        "imie": imie_ucznia,
        "nazwisko": nazwisko_ucznia,
        "klasa": klasa_ucznia
    }]
    uczniowie.append(nowy_uczen)

def tworzenie_nauczyciela():
    imie_nauczyciela = input("Podaj imie nauczyciela, którego chcesz dodać: ")
    nazwisko_nauczyciela = input("Podaj nazwisko nauczyciela, którego chcesz dodać: ")
    nazwa_przedmiotu = input("Podaj nazwę przedmiotu, którego dany nauczyciel uczy: ")
    nauczane_klasy = input("Podaj w jakich klasach uczy nauczyciel") # nie jest to jedno po drugim tak jak w zadaniu

    nowy_nauczyciel = [{
        "imie": imie_nauczyciela,
        "nazwisko": nazwisko_nauczyciela,
        "nazwa_przedmiotu": nazwa_przedmiotu,
        "prowadzone_klasy": nauczane_klasy
    }]
    nauczyciele.append(nowy_nauczyciel)

def tworzenie_wychowawcy():
    imie_wychowawcy = input("Podaj imie wychowawcy, którego chcesz wprowadzić: ")
    nazwisko_wychowawcy = input("Podaj nazwisko wychowawcy, którego chcesz wprowadzić: ")
    wychowawstwo = input("Podaj jakiej klasy jest wychowawcą: ")

    nowy_wychowawca = [{
        "imie": imie_wychowawcy,
        "nazwisko": nazwisko_wychowawcy,
        "wychowawstwo": wychowawstwo
    }]
    wychowawca.append(nowy_wychowawca)

def wyswietlanie_klasy():   #nie działa, nie wiem jak się do tego zabrać
    wybor_klasy = input("Podaj klase: ")

def wyswietlenie_ucznia():
    imie_ucznia = input("Podaj imie ucznia: ")
    nazwisko_ucznia = input("Podaj nazwisko ucznia: ")
    print(f"Uczeń o imieniu {imie_ucznia} i nazwisku {nazwisko_ucznia} ma  ")



while True:
    wybor_uzytkownika = input("Wybierz jedna z dostepnych opcji:\n1. utwórz\n2. zarzadzaj\n3. koniec\n")

    #opcja UTWÓRZ(działa, ale klasy nauczyciela do poprawy)
    if wybor_uzytkownika == "1" or wybor_uzytkownika == "utwórz":
        wybor_polecenia = input("Wybierz kogo chcesz utworzyć:\n1. uczeń\n2. nauczyciel\n3. wychowawca\n4. koniec")
        #tworzenie ucznia
        if wybor_polecenia == "1" or wybor_polecenia == "uczeń":
            tworzenie_ucznia()

        #tworzenie nauczyciela
        elif wybor_polecenia == "2" or wybor_polecenia == "nauczyciel":
            tworzenie_nauczyciela()

        #tworzenie_wychowawcy
        elif wybor_polecenia == "3" or wybor_polecenia == "wychowawca":
            tworzenie_wychowawcy()

        #powrót do pierwszego menu, koniec tworzenia
        elif wybor_polecenia == "4" or wybor_polecenia == "koniec":
            pass

    elif wybor_uzytkownika == "2" or wybor_uzytkownika == "zarzadzaj":
        wybor_zarzadzania = input("Wybierz jedna z dostępnych opcji:\n1. klasa\n2. uczen\n3. nauczyciel\n4. wychowawca\n5. koniec")
        #nie działa
        if wybor_zarzadzania == "1" or wybor_zarzadzania == "klasa":
            pass
        elif


        #powrót do menu głównego
        elif wybor_uzytkownika == "5" or wybor_zarzadzania == "koniec":
            pass

    #zakończeni programu (działa)
    elif wybor_uzytkownika == "3" or wybor_uzytkownika == "koniec":
        break

