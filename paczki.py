# Pytanie użytkownika ile przedmiotów chce wysłać
liczba_przedmiotow = int(input("Ile przedmiotów chcesz wysłać? "))

# Inicjalizacja zmiennych
laczna_waga_przedmiotow = 0.0
liczba_paczek = 1
pojemnosc_biezacej_paczki = 0.0
maksymalna_niewykorzystana_pojemnosc = 0.0
numer_paczki_z_maksymalna_niewykorzystana_pojemnoscia = 1

# Pytanie użytkownika o wagę każdego przedmiotu
for przedmiot in range(liczba_przedmiotow):
    while True:
        waga_przedmiotu = float(input("Podaj wagę przedmiotu (1-10 kg): "))

        # Jeśli waga przedmiotu jest poza zakresem, proś o ponowne podanie
        if waga_przedmiotu > 10.0:
            print("Podana waga jest większa niż 10 kg. Podaj wagę z przedziału 1-10 kg.")
            continue
        elif waga_przedmiotu < 1.0:
            print("Podana waga jest mniejsza niż 1 kg. Podaj wagę z przedziału 1-10 kg.")
            continue
        break

    # Dodajemy wagę do sumy całkowitej
    laczna_waga_przedmiotow += waga_przedmiotu

    # Sprawdzanie, czy waga przedmiotu mieści się w aktualnej paczce
    if waga_przedmiotu + pojemnosc_biezacej_paczki > 20.0:
        # Sprawdzenie niewykorzystanej pojemności przed zamknięciem paczki
        niewykorzystana_pojemnosc = 20.0 - pojemnosc_biezacej_paczki
        if niewykorzystana_pojemnosc > maksymalna_niewykorzystana_pojemnosc:
            maksymalna_niewykorzystana_pojemnosc = niewykorzystana_pojemnosc
            numer_paczki_z_maksymalna_niewykorzystana_pojemnoscia = liczba_paczek

        # Rozpoczęcie nowej paczki
        liczba_paczek += 1
        pojemnosc_biezacej_paczki = waga_przedmiotu
    else:
        pojemnosc_biezacej_paczki += waga_przedmiotu

# Sprawdzenie niewykorzystanej pojemności ostatniej paczki
niewykorzystana_pojemnosc = 20.0 - pojemnosc_biezacej_paczki
if niewykorzystana_pojemnosc > maksymalna_niewykorzystana_pojemnosc:
    maksymalna_niewykorzystana_pojemnosc = niewykorzystana_pojemnosc
    numer_paczki_z_maksymalna_niewykorzystana_pojemnoscia = liczba_paczek

# Wyświetlanie podsumowania
print(f"\nPodsumowanie:")
print(f"Liczba wysłanych paczek: {liczba_paczek}")
print(f"Łączna waga wysłanych przedmiotów: {laczna_waga_przedmiotow:.2f} kg")
print(f"Liczba niewykorzystanych kilogramów: {liczba_paczek * 20.0 - laczna_waga_przedmiotow:.2f} kg")
print(
    f"Paczka nr {numer_paczki_z_maksymalna_niewykorzystana_pojemnoscia} miała najwięcej niewykorzystanej pojemności: {maksymalna_niewykorzystana_pojemnosc:.2f} kg")
