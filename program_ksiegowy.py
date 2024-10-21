# Napisz program, który będzie rejestrował operacje na koncie firmy i stan magazynu.
#
# Program po uruchomieniu wyświetla informację o dostępnych komendach:
#
# saldo
# sprzedaż
# zakup
# konto
# lista
# magazyn
# przegląd
# koniec
#
# Po wprowadzeniu odpowiedniej komendy, aplikacja zachowuje się w unikalny sposób dla każdej z nich:
#
# saldo - Program pobiera kwotę do dodania lub odjęcia z konta.
# sprzedaż - Program pobiera nazwę produktu, cenę oraz liczbę sztuk. Produkt musi znajdować się w magazynie. Obliczenia respektuje względem konta i magazynu (np. produkt "rower" o cenie 100 i jednej sztuce spowoduje odjęcie z magazynu produktu "rower" oraz dodanie do konta kwoty 100).
# zakup - Program pobiera nazwę produktu, cenę oraz liczbę sztuk. Produkt zostaje dodany do magazynu, jeśli go nie było. Obliczenia są wykonane odwrotnie do komendy "sprzedaz". Saldo konta po zakończeniu operacji „zakup” nie może być ujemne.
# konto - Program wyświetla stan konta.
# lista - Program wyświetla całkowity stan magazynu wraz z cenami produktów i ich ilością.
# magazyn - Program wyświetla stan magazynu dla konkretnego produktu. Należy podać jego nazwę.
# przegląd - Program pobiera dwie zmienne „od” i „do”, na ich podstawie wyświetla wszystkie wprowadzone akcje zapisane pod indeksami od „od” do „do”. Jeżeli użytkownik podał pustą wartość „od” lub „do”, program powinien wypisać przegląd od początku lub/i do końca. Jeżeli użytkownik podał zmienne spoza zakresu, program powinien o tym poinformować i wyświetlić liczbę zapisanych komend (żeby pozwolić użytkownikowi wybrać odpowiedni zakres).
# koniec - Aplikacja kończy działanie.
#
# Dodatkowe wymagania:
#
# Aplikacja od uruchomienia działa tak długo, aż podamy komendę "koniec".
# Komendy saldo, sprzedaż i zakup są zapamiętywane przez program, aby móc użyć komendy "przeglad".
# Po wykonaniu dowolnej komendy (np. "saldo") aplikacja ponownie wyświetla informację o dostępnych komendach, a także prosi o wprowadzenie jednej z nich.
# Zadbaj o błędy, które mogą się pojawić w trakcie wykonywania operacji (np. przy komendzie "zakup" jeśli dla produktu podamy ujemną kwotę, aplikacja powinna wyświetlić informację o niemożności wykonania operacji i jej nie wykonać). Zadbaj też o prawidłowe typy danych.

stan_konta = 10_000
przeglad = ["wpłata na konto 10000 zł", "proba", "proba"]
stan_magazynowy = [
    {"nazwa":"dlugopis",
     "stan_magazynu":10,
     "cena":float(1)
    },
    {"nazwa":"zeszyt",
     "stan_magazynu":15,
     "cena":2.0
    }
]

while True:
    wybor_uzytkownika = input("Wybierz co chcesz zrobić:\n1. saldo\n2. sprzedaż\n3. zakup\n4. konto\n5. lista\n6. magazyn\n7. przeglad\n8. koniec\n")

    #dodanie/ odejmowanie z konta (działa)
    if wybor_uzytkownika == "1" or wybor_uzytkownika == "saldo":
        kwota = float(input("Podaj kwote o którą chcesz zmienić obecne saldo: "))
        if stan_konta + kwota < 0:
            print("Nie możesz wykonać żądanej operacji, brak wystarczających środków na koncie.")
            przeglad.append("Proba odjecia zbyt duzej kwoty.")
        else:
            stan_konta += kwota
            print(f"Dodałeś do konta {kwota}.\n")
            przeglad.append(f"Dodanie {kwota} zł.")

    # sprzedaż produktów z magazynu(nie działa)
    elif wybor_uzytkownika == "2" or wybor_uzytkownika == "sprzedaz":
        nazwa_produktu = input("Podaj nazwe produktu ktory chcesz kupić: ")
        ilosc_produktu = int(input("Podaj ile sztuk produktu chcesz kupić: "))
        cena_przedmiotu = float(input("Podaj cene jednostkową produktu: "))
        for produkt in stan_magazynowy:
            if produkt.get("nazwa") == nazwa_produktu and produkt.get("stan_magazynu") >= ilosc_produktu and produkt.get("cena") == cena_przedmiotu:
                produkt["stan_magazynu"] -= ilosc_produktu
                stan_konta += produkt.get("cena") * ilosc_produktu
                print(f"Zakupiłeś {nazwa_produktu} w ilosci sztuk: {ilosc_produktu}.")
                przeglad.append(f"Sprzedaż {nazwa_produktu} w ilości {ilosc_produktu} za kwotę {cena_przedmiotu * ilosc_produktu} zł.")
                break

            else:
                print("Nie możesz zakupić podanego produktu w podanej ilosci.")
                przeglad.append("Nieudana proba zakupu.")
                break

            # elif produkt.get("nazwa") == nazwa_produktu and produkt.get("stan_magazynu") < ilosc_produktu and produkt.get("cena") == cena_przedmiotu:
            #     print("Nie mamy wystarczającej ilości produktu w magazynie")
            # elif produkt.get("nazwa") == nazwa_produktu and produkt.get("stan_magazynu") < ilosc_produktu and produkt.get("cena") != cena_przedmiotu:
            #     print("Podano błędną cenę.")
            # elif produkt.get("nazwa") != nazwa_produktu:
            #     print("Podano błędną nazwę produktu.")


    # Zakup nowych produktow(działa)
    elif wybor_uzytkownika == "3" or wybor_uzytkownika == "zakup":
        nazwa_zakupionego_produktu = input("Wpisz co zakupiłeś: ")
        ilosc_zakupionego_produktu = int(input("Podaj ilość zakupionego produktu: "))
        cena_jednostkowa = float(input("Podaj cene jednostkową zakupionego przedmiotu: "))
        cena_sprzedażowa = float(input("Podaj cene sprzedażową produktu: "))
        if cena_jednostkowa * ilosc_zakupionego_produktu > stan_konta:
            print("Cena zakupu przewyższa obecny stan konta.")
            przeglad.append("Próba zakupu zza drogich produktów.")
            continue

        stan_magazynowy.append({
            "nazwa": nazwa_zakupionego_produktu,
            "stan_magazynu": ilosc_zakupionego_produktu,
            "cena": cena_jednostkowa
        })
        stan_konta -= ilosc_zakupionego_produktu * cena_jednostkowa
        przeglad.append(f"Zakup {nazwa_zakupionego_produktu} w ilości: {ilosc_zakupionego_produktu}.")

    #Wyświetlenie stanu konta(działa)
    elif wybor_uzytkownika == "4" or wybor_uzytkownika == "konto":
        print(f"Stan konta wynosi: {stan_konta}.\n")
        przeglad.append("Wyświetlenie stanu konta.")

    #wyświetlenie stanu magazynowego (działa)
    elif wybor_uzytkownika == "5" or wybor_uzytkownika == "lista":
        print(stan_magazynowy)
        przeglad.append("Sprawdzenie stanu magazynowego.")

    #sprawdzenie stanu magazynowego konkretnego produktu (działa)
    elif wybor_uzytkownika == "6" or wybor_uzytkownika == "magazyn":
        stan_produktu = input("Podaj nazwę produktu, którego chcesz sprawdzić stan magazynowy: ")
        for stan in stan_magazynowy:
            if stan.get("nazwa") == stan_produktu:
            #     print(stan["nazwa"])
            #     print(stan["stan_magazynu"])
            #     print(stan["cena"])
                print(stan)
                przeglad.append(f"Sprawdzenie stanu produktu: {stan_produktu}.")

    #przeglad operacji(działą)
    elif wybor_uzytkownika == "7" or wybor_uzytkownika == "przeglad":
        od = input("Podaj od którego momentu chcesz wyswietlić historię: ")
        do = input("Podaj do którego momentu chcesz wyswietlić historię: ")

        if len(od) > 0:
            od = int(od)
        else:
            od = 0
        if len(do) > 0:
            do = int(do)
        else:
            do = len(przeglad)
        if od >= 0  and do <= len(przeglad) and od < len(przeglad):
            print(przeglad[od:do])

        else:
            print(f"Podane błędne wartości. Podaj wartości z zakresu od 0 do {len(przeglad)}. ")

    #zakończenie programu(działa)
    elif wybor_uzytkownika == "8":
        break

    else:
        print("Wybrano niewłaściwą opcję.\n")