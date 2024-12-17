# Napisz program, który sprawdzi, czy danego dnia będzie padać. Użyj do tego poniższego API. Aplikacja ma działać następująco:
#
# Program pyta dla jakiej daty należy sprawdzić pogodę. Data musi byc w formacie YYYY-mm-dd, np. 2022-11-03.
# W przypadku nie podania daty, aplikacja przyjmie za poszukiwaną datę następny dzień.
# Aplikacja wykona zapytanie do API w celu poszukiwania stanu pogody.
# Istnieją trzy możliwe informacje dla opadów deszczu:
# Będzie padać (dla wyniku większego niż 0.0)
# Nie będzie padać (dla wyniku równego 0.0)
# Nie wiem (gdy wyniku z jakiegoś powodu nie ma lub wartość jest ujemna)
# Będzie padać
# Nie będzie padać
# Nie wiem
# Wyniki zapytań powinny być zapisywane do pliku. Jeżeli szukana data znajduje sie juz w pliku, nie wykonuj zapytania do API, tylko zwróć wynik z pliku.
#
# URL do API:
# https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=rain&daily=rain_sum&timezone=Europe%2FLondon&start_date={searched_date}&end_date={searched_date}
#
# W URL należy uzupełnić parametry: latitude, longitude oraz searched_date

import datetime
from utils import retrive_data_from_api
from file_handler import FileHandler

from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="AleksanderO")
city = input("Podaj miasto: ")
location = geolocator.geocode(city)
print(location.address)
print((location.latitude, location.longitude))
print(location.raw)


file_hanlder = FileHandler(file="date_data.json")

latitude = location.latitude
longitude = location.longitude
searched_data = input("Podaj date: ")
city_location = location.address

data_in_memory = file_hanlder.get_data_from_file(searched_data, city_location)
if data_in_memory:
    if data_in_memory["rain_data"] > 0:
        print("Będzie padać.")
    elif data_in_memory["rain_data"] == 0:
        print("Nie będzie padać")
    else:
        print("Nie wiem")


else:
    czy_bedzie_padac = retrive_data_from_api(searched_data, latitude, longitude)
    file_hanlder.add_new_date_to_data(searched_data, czy_bedzie_padac, city_location)
    file_hanlder.save_data_to_file()
    print(czy_bedzie_padac)

    if czy_bedzie_padac["rain_data"] > 0:
        print("Będzie padać.")
    elif czy_bedzie_padac["rain_data"] == 0:
        print("Nie będzie padać")
    else:
        print("Nie wiem")
