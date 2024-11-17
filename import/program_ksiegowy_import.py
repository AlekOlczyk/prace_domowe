# Na podstawie zadania z lekcji 5 (operacje na koncie, sprzedaż/zakup itp.) należy zaimplementować poniższą część:
#
# Saldo konta oraz magazyn mają zostać zapisane do pliku tekstowego, a przy kolejnym uruchomieniu programu ma zostać odczytany.
# Zapisać należy również historię operacji (przegląd), która powinna być rozszerzana przy każdym kolejnym uruchomieniu programu.

from file_handler import FileHandler

file_handler = FileHandler(data_file="dane.json", history_file="historia.json")
data = file_handler.load_data_from_data_file()
history = file_handler.load_data_from_history_file()

stan_konta = data.get("saldo")
przeglad = history
stan_magazynowy = data.get("stan_magazynowy")

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

    # sprzedaż produktów z magazynu(działa)
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
            if produkt.get("nazwa") != nazwa_produktu and produkt.get("stan_magazynu") >= ilosc_produktu and produkt.get("cena") == cena_przedmiotu:
                print("Podano błędną nazwe produktu, spróbuj ponownie.")
                przeglad.append("Nieudana próba zakupu: błędna nazwa.")
            if produkt.get("nazwa") == nazwa_produktu and produkt.get("stan_magazynu") < ilosc_produktu and produkt.get("cena") == cena_przedmiotu:
                print("Nie mamy wystarczającej ilości produtku w magazynie.")
                przeglad.append("Nieudana próba zakupu: żądana ilość jest zbyt duża.")
            if produkt.get("nazwa") == nazwa_produktu and produkt.get("stan_magazynu") >= ilosc_produktu and produkt.get("cena") != cena_przedmiotu:
                print("Podano błędną cene.")
                przeglad.append("Nieudana próba zakupu: podano błędna cene.")
            if produkt.get("nazwa") == nazwa_produktu and produkt.get("stan_magazynu") < ilosc_produktu and produkt.get("cena") != cena_przedmiotu:
                print("Nie mamy wystarczającej ilości produtku w magazynie. Podano blędną cene.")
                przeglad.append("Nieudana próba zakupu: żądana ilość jest zbyt duża oraz podano błędna cene.")


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

file_handler.save_data_to_data_file(balance=stan_konta, stock= stan_magazynowy)
file_handler.save_history_to_history_file(history=przeglad)

