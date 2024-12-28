# Zoptymalizuj kod z poprzedniego zadania z pogodą.
#
# Utwórz klasę WeatherForecast, która będzie służyła do odczytywania i zapisywania pliku, a także odpytywania API.
#
# Obiekt klasy WeatherForecast dodatkowo musi poprawnie implementować cztery metody:
#
#  __setitem__
#  __getitem__
#  __iter__
#  items
#
# Wykorzystaj w kodzie poniższe zapytania:
#
# weather_forecast[date] da odpowiedź na temat pogody dla podanej daty
# weather_forecast.items() zwróci generator tupli w formacie (data, pogoda) dla już zapisanych rezultatów przy wywołaniu
# weather_forecast to iterator zwracający wszystkie daty, dla których znana jest pogoda

class WeatherForecast:
    def __init__(self, file):
        self.file = file
        self.data = self.load_data_from_file()

    def load_data_from_file(self):
        with open(self.file) as file:
            data = json.loads(file.read())
            return data

    def save_data_to_file(self):
        with open(self.file) as file:
            file.write(json.dumps(self.data))
