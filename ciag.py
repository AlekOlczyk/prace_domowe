# Ciąg Collatza zdefiniowany jest następująco:
# Rozpoczynamy od podanej ze standardowego wejścia liczby x (od 1 do 100).
# Jeśli x jest liczbą parzystą, to kolejny wyraz ciągu będzie obliczony jako x/2.
# W przeciwnym przypadku kolejny wyraz ciągu będzie równy 3x+1.
# W ten sam sposób obliczamy kolejne wyrazy ciągu, aż pojawi się liczba 1.
#
# Napisz program, który wypisze długość ciągu Collatza dla podanego ze standardowego wejścia x.
# X może przyjmować wartości od 1 do 100.

# podanie liczby x
liczba = int(input("Podaj liczbe z przedziału od 1 do 100: "))
dlugosc_ciagu = 0
if 1 <= liczba <= 100:
    while liczba != 1:
        if liczba % 2 == 0:
            liczba = liczba // 2
        else:
            liczba = 3 * liczba + 1
        print(liczba)
        dlugosc_ciagu += 1
else:
    print("Liczba nie jest z zakresu od 1 do 100.")
print(f"Długość ciagu wynosi {dlugosc_ciagu}.")


