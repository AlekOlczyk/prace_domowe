# Napisz program do obsługi ładowarki paczek. Po uruchomieniu, aplikacja pyta ile paczek chcesz wysłać, a następnie wymaga podania wagi dla każdej z nich.
#
# Na koniec działania program powinien wyświetlić w podsumowaniu:
#
# Liczbę paczek wysłanych
# Liczbę kilogramów wysłanych
# Suma "pustych" - kilogramów (brak optymalnego pakowania). Liczba paczek * 20 - liczba kilogramów wysłanych
# Która paczka miała najwięcej "pustych" kilogramów, jaki to był wynik
#
# Restrykcje:
#
# Waga elementów musi być z przedziału od 1 do 10 kg.
# Każda paczka może maksymalnie zmieścić 20 kilogramów towaru.
# W przypadku, jeżeli dodawany element przekroczy wagę towaru, ma zostać dodany do nowej paczki, a obecna wysłana.
# W przypadku podania wagi elementu mniejszej od 1kg lub większej od 10kg, dodawanie paczek zostaje zakończone i wszystkie paczki są wysłane. Wyświetlane jest podsumowanie.

#Pytanie użytkownika ile przedmiotow chce wyslac
ilosc_przedmiotow = int(input("Ile przedmiotow chesz wysłać? "))

# paczka = 20
liczba_paczek = 1
pojemnosc_biezacej_paczki = 0
maksymalna_niewykorzystana_pojemnosc = 0
numer_paczki_z_maksymalna_niewykorzystana_pojemnoscia = 1
laczna_waga_przedmiotow = 0
#Pytanie użytkownika jaka wage ma dany przedmiot
for przedmiot in range(ilosc_przedmiotow):

    waga_przedmiotu = int(input("Podaj wage przedmiotu: "))
    if waga_przedmiotu > 10 or waga_przedmiotu < 1:
        ilosc_przedmiotow = przedmiot
        break
    laczna_waga_przedmiotow += waga_przedmiotu
    if waga_przedmiotu + pojemnosc_biezacej_paczki > 20:
        if 20 - pojemnosc_biezacej_paczki > maksymalna_niewykorzystana_pojemnosc:
            maksymalna_niewykorzystana_pojemnosc = 20 - pojemnosc_biezacej_paczki
            numer_paczki_z_maksymalna_niewykorzystana_pojemnoscia = liczba_paczek
            pojemnosc_biezacej_paczki = waga_przedmiotu
        liczba_paczek += 1
    else:
        pojemnosc_biezacej_paczki += waga_przedmiotu
if 20 - pojemnosc_biezacej_paczki > maksymalna_niewykorzystana_pojemnosc:
    maksymalna_niewykorzystana_pojemnosc = 20 - pojemnosc_biezacej_paczki
    numer_paczki_z_maksymalna_niewykorzystana_pojemnoscia = liczba_paczek
    pojemnosc_biezacej_paczki = waga_przedmiotu

print(f"Chesz wysłać następującą liczbę przedmiotów: {ilosc_przedmiotow}.")
print(f"Liczba wysłanych paczek wynosi: {liczba_paczek}")
print(f"Łączna waga przedmiotów wynosi {laczna_waga_przedmiotow} kg.")
# print(f"Pojemność bieżacej paczki wynosi {pojemnosc_biezacej_paczki} kg.")
print(f"Liczba niewykorzystanych kilogramów wynosi: {liczba_paczek*20-laczna_waga_przedmiotow}")
print(f"Numer paczki z największą niewykorzystana pojemnością to {numer_paczki_z_maksymalna_niewykorzystana_pojemnoscia} i wynosi {liczba_paczek*20-laczna_waga_przedmiotow}")



