import requests
from pprint import pprint

def retrive_data_from_api(latitude, longitude, searched_date):
    url_adress = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=rain&daily=rain_sum&timezone=Europe%2FLondon&start_date={searched_date}&end_date={searched_date}"
    response = requests.get(url_adress)
    # print(response)             #wyswietla response 200 jeżeli jest wszystko git
    # print(response.json())      #wyswietla wszystkie informacje
    if response.status_code == 200:
        print("Udało się pobrać dane.")
        print(response.json())
        return parse_data_from_api(response.json())
    else:
        print("Nie udało się pobrać danych.")
        print(response.json())
        print(response.status_code)

def parse_data_from_api(response_text):
    # pprint(response_text)
    # print(response_text["daily"]["rain_sum"][0])
    return {
        "bedzie_padac": response_text["daily"]["rain_sum"][0]
    }
