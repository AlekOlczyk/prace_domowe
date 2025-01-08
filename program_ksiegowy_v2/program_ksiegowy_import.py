from manager import manager

@manager.assign("zmiana_salda")
def zmiena_salda(manager):
    kwota = float(input("Podaj kwote o którą chcesz zmienić obecne saldo: "))
    if manager.saldo + kwota < 0:
        print("Nie możesz wykonać żądanej operacji, brak wystarczających środków na koncie.")
        manager.historia.append("Proba odjecia zbyt duzej kwoty.")
    else:
        manager.saldo += kwota
        print(f"Dodałeś do konta {kwota}.\n")
        manager.historia.append(f"Dodanie {kwota} zł.")

@manager.assign("sprzedaz")
def sprzedaz(manager):
    nazwa_produktu = input("Podaj nazwe produktu ktory chcesz kupić: ")
    ilosc_produktu = int(input("Podaj ile sztuk produktu chcesz kupić: "))
    cena_przedmiotu = float(input("Podaj cene jednostkową produktu: "))
    for produkt in manager.stan_magazynowy:
        if produkt.get("nazwa") == nazwa_produktu and produkt.get("stan_magazynu") >= ilosc_produktu and produkt.get(
                "cena") == cena_przedmiotu:
            produkt["stan_magazynu"] -= ilosc_produktu
            manager.saldo += produkt.get("cena") * ilosc_produktu
            print(f"Zakupiłeś {nazwa_produktu} w ilosci sztuk: {ilosc_produktu}.")
            manager.historia.append(
                f"Sprzedaż {nazwa_produktu} w ilości {ilosc_produktu} za kwotę {cena_przedmiotu * ilosc_produktu} zł.")
            break
        if produkt.get("nazwa") != nazwa_produktu and produkt.get("stan_magazynu") >= ilosc_produktu and produkt.get(
                "cena") == cena_przedmiotu:
            print("Podano błędną nazwe produktu, spróbuj ponownie.")
            manager.historia.append("Nieudana próba zakupu: błędna nazwa.")
        if produkt.get("nazwa") == nazwa_produktu and produkt.get("stan_magazynu") < ilosc_produktu and produkt.get(
                "cena") == cena_przedmiotu:
            print("Nie mamy wystarczającej ilości produtku w magazynie.")
            manager.historia.append("Nieudana próba zakupu: żądana ilość jest zbyt duża.")
        if produkt.get("nazwa") == nazwa_produktu and produkt.get("stan_magazynu") >= ilosc_produktu and produkt.get(
                "cena") != cena_przedmiotu:
            print("Podano błędną cene.")
            manager.historia.append("Nieudana próba zakupu: podano błędna cene.")
        if produkt.get("nazwa") == nazwa_produktu and produkt.get("stan_magazynu") < ilosc_produktu and produkt.get(
                "cena") != cena_przedmiotu:
            print("Nie mamy wystarczającej ilości produtku w magazynie. Podano blędną cene.")
            manager.historia.append("Nieudana próba zakupu: żądana ilość jest zbyt duża oraz podano błędna cene.")

@manager.assign("zakup")    #continue nie pasuje
def zakup(manager):
    nazwa_zakupionego_produktu = input("Wpisz co zakupiłeś: ")
    ilosc_zakupionego_produktu = int(input("Podaj ilość zakupionego produktu: "))
    cena_jednostkowa = float(input("Podaj cene jednostkową zakupionego przedmiotu: "))
    cena_sprzedażowa = float(input("Podaj cene sprzedażową produktu: "))
    if cena_jednostkowa * ilosc_zakupionego_produktu > manager.saldo:
        print("Cena zakupu przewyższa obecny stan konta.")
        manager.historia.append("Próba zakupu zza drogich produktów.")
        continue


    manager.stan_magazynowy.append({
        "nazwa": nazwa_zakupionego_produktu,
        "stan_magazynu": ilosc_zakupionego_produktu,
        "cena": cena_jednostkowa
    })
    manager.saldo -= ilosc_zakupionego_produktu * cena_jednostkowa
    manager.historia.append(f"Zakup {nazwa_zakupionego_produktu} w ilości: {ilosc_zakupionego_produktu}.")

@manager.assign("konto")
def konto(manager):
    print(f"Stan konta wynosi: {manager.saldo}.\n")
    manager.historia.append("Wyświetlenie stanu konta.")

@manager.assign("lista")
def lista(manager):
    print(manager.stan_magazynowy)
    manager.historia.append("Sprawdzenie stanu magazynowego.")

@manager.assign("magazyn")
def magazyn(manager):
    stan_produktu = input("Podaj nazwę produktu, którego chcesz sprawdzić stan magazynowy: ")
    for stan in manager.stan_magazynowy:
        if stan.get("nazwa") == stan_produktu:
            print(stan)
            manager.historia.append(f"Sprawdzenie stanu produktu: {stan_produktu}.")

@manager.assign("historia")     #czemu jest w użyciu 20 razy
def historia(manager):
    od = input("Podaj od którego momentu chcesz wyswietlić historię: ")
    do = input("Podaj do którego momentu chcesz wyswietlić historię: ")

    if len(od) > 0:
        od = int(od)
    else:
        od = 0
    if len(do) > 0:
        do = int(do)
    else:
        do = len(manager.historia)
    if od >= 0 and do <= len(manager.historia) and od < len(manager.historia):
        print(manager.historia[od:do])

    else:
        print(f"Podane błędne wartości. Podaj wartości z zakresu od 0 do {len(manager.historia)}. ")



while True:
    wybor_uzytkownika = input("Wybierz co chcesz zrobić:\n1. saldo\n2. sprzedaż\n3. zakup\n4. konto\n5. lista\n6. magazyn\n7. manager.historia\n8. koniec\n")

    #dodanie/ odejmowanie z konta (działa)
    if wybor_uzytkownika == "1" or wybor_uzytkownika == "saldo":
        manager.execute("zmiana_salda")

    # sprzedaż produktów z magazynu(działa)
    elif wybor_uzytkownika == "2" or wybor_uzytkownika == "sprzedaz":
        manager.execute("sprzedaz")


    # Zakup nowych produktow(działa)
    elif wybor_uzytkownika == "3" or wybor_uzytkownika == "zakup":
        nazwa_zakupionego_produktu = input("Wpisz co zakupiłeś: ")
        ilosc_zakupionego_produktu = int(input("Podaj ilość zakupionego produktu: "))
        cena_jednostkowa = float(input("Podaj cene jednostkową zakupionego przedmiotu: "))
        cena_sprzedażowa = float(input("Podaj cene sprzedażową produktu: "))
        if cena_jednostkowa * ilosc_zakupionego_produktu > manager.saldo:
            print("Cena zakupu przewyższa obecny stan konta.")
            manager.historia.append("Próba zakupu zza drogich produktów.")
            continue

        manager.stan_magazynowy.append({
            "nazwa": nazwa_zakupionego_produktu,
            "stan_magazynu": ilosc_zakupionego_produktu,
            "cena": cena_jednostkowa
        })
        manager.saldo -= ilosc_zakupionego_produktu * cena_jednostkowa
        manager.historia.append(f"Zakup {nazwa_zakupionego_produktu} w ilości: {ilosc_zakupionego_produktu}.")

    #Wyświetlenie stanu konta(działa)
    elif wybor_uzytkownika == "4" or wybor_uzytkownika == "konto":
        manager.execute("konto")

    #wyświetlenie stanu magazynowego (działa)
    elif wybor_uzytkownika == "5" or wybor_uzytkownika == "lista":
        manager.execute("lista")

    #sprawdzenie stanu magazynowego konkretnego produktu (działa)
    elif wybor_uzytkownika == "6" or wybor_uzytkownika == "magazyn":
        manager.execute("magazyn")

    #manager.historia operacji(działą)
    elif wybor_uzytkownika == "7" or wybor_uzytkownika == "historia":
        manager.execute("historia")

    #zakończenie programu(działa)
    elif wybor_uzytkownika == "8" or wybor_uzytkownika == "koniec":
        break

    else:
        print("Wybrano niewłaściwą opcję.\n")

manager.file_handler.save_data_to_data_file(balance=manager.saldo, stock=manager.stan_magazynowy)
manager.file_handler.save_history_to_history_file(history=manager.historia)

