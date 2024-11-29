# Napisz program, który odczyta wejściowy plik CSV, następnie zmodyfikuje go i wyświetli w terminalu jego zawartość,
# a na końcu zapisze w wybranej lokalizacji.
#
# Uruchomienie programu przez terminal:
# python reader.py <plik_wejsciowy> <plik_wyjsciowy> <zmiana_1> <zmiana_2> ... <zmiana_n>
#
#  <plik_wejsciowy> - nazwa pliku, który ma zostać odczytany, np. in.csv
#  <plik_wyjsciowy> - nazwa pliku, do którego ma zostać zapisana zawartość, np. out.csv
# <zmiana_x> - Zmiana w postaci "x,y,wartosc" - x (kolumna) oraz y (wiersz) są współrzędnymi liczonymi od 0,
# natomiast "wartosc" zmianą która ma trafić na podane miejsce.
#
# Przykładowy plik wejściowy znajduje się w repozytorium pod nazwą "in.csv".
#
# Przykład działania:
# python reader.py in.csv out.csv 0,0,gitara 3,1,kubek 1,2,17 3,3,0
# Z pliku in.csv:
# drzwi,3,7,0
# kanapka,12,5,1
# pedzel,22,34,5
# plakat,czerwony,8,kij
# Ma wyjść plik out.csv:
# gitara,3,7,0
# kanapka,12,5,kubek
# pedzel,17,34,5
# plakat,czerwony,8,0
import csv
import sys

def zmiany_csv(file_in= "in.csv",file_out= "out.csv",zmiany=[]):

    rows = []

    with open(file_in) as file:
        reader = csv.reader(file)

        for row in reader:
            rows.append(row)

    new_rows = []

    for r_idx,row in enumerate(rows):
        new_row = []
        for c_idx, val in enumerate(row):
            print(f"Wiersz: {r_idx}, kolumna: {c_idx}, wartość: {val}")
            new_row.append(val)
            for zmiana in zmiany:
                zmiana_lista = zmiana.split(",")
                zmiana_wiersz = int(zmiana_lista[0])
                zmiana_kolumna = int(zmiana_lista[1])
                zmiana_wartosc = zmiana_lista[2]
                if r_idx == zmiana_wiersz and c_idx == zmiana_kolumna:
                    print(f"nowa wartosc: {zmiana_wartosc}")
                    new_row[c_idx] = zmiana_wartosc

        new_rows.append(new_row)

    with open(file_out, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(new_rows)


if __name__ == "__main__":

    # print("hello")
    args = sys.argv
    if len(args) > 3:
        file_in_path = args[1]
        file_out_path = args[2]
        changes = args[3:]
        print(f"plik wejsciowy: {file_in_path}, plik wyjsciowy: {file_out_path}")
        print(f"Zmiany: {changes}")
        # zmiany_test = ["3,1,kubek", "1,2,zupa", "2,1,dlugopis"]
        zmiany_csv(file_in_path, file_out_path, changes)
    else:
        print("Błędna liczba argumentów.")

