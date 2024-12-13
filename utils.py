import requests
from pprint import pprint

def retrive_data_from_api(searched_date):
    url_adress = f"https://api.open-meteo.com/v1/forecast?latitude=52&longitude=21&hourly=rain&daily=rain_sum&timezone=Europe%2FLondon&start_date={searched_date}&end_date={searched_date}"
    response = requests.get(url_adress)
    # print(response)             #wyswietla response 200 jeżeli jest wszystko git
    # print(response.json())      #wyswietla wszystkie informacje
    if response.status_code == 200:
        print("Udało się pobrać dane.")
        # print(response.json())
        return parse_data_from_api(response.json())
    else:
        print("Nie udało się pobrać danych.")
        print(response.json())
        print(response.status_code)

def parse_data_from_api(response_text):
    # pprint(response_text)
    # print(response_text["daily"]["rain_sum"][0])
    return {
        "rain_data": response_text["daily"]["rain_sum"][0]
    }

# 1.wczytac plik z baza danych txt
# 2.jezeli jest pusty zapisz nowa date
# 3.jezeli nie jest pusty sprawdz czy jest podana data
# 4.jezeli jest podana data to ja zwroc
# 5.jezeli nie ma podanej daty to wyslij zapytanie do api
# wszystko jedna funkcja

