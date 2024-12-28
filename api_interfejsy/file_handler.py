import json


class FileHandler:
    def __init__(self, file):
        self.file = file
        self.data = self.load_data_from_file()

    def load_data_from_file(self):
        with open(self.file) as file:
            data = json.loads(file.read())
            return data

    def save_data_to_file(self):
        with open(self.file, mode="w") as file:
            file.write(json.dumps(self.data))

    def add_new_date_to_data(self, city, searched_date, data):
        self.data.setdefault(city, {})
        self.data[city][searched_date] = data

    def get_data_from_file(self, city, searched_data):
        # for key,value in self.data.items():
        #     if key == searched_data:
        #         return value              #to samo co niżej
        if city in self.data.keys():
            if searched_data in self.data[city].keys():
                return self.data.get(searched_data)

    def __setitem__(self, key, value):
        city = key[0]
        date = key[1]
        if not self.data.get(city):
            self.data[city] = {}
        self.data[city][date] = value

    def __getitem__(self, item):
        city = item[0]
        key = item[1]
        return self.data.get(city, {}).get(key)

    def __iter__(self):
        return iter(self.data)

    def items(self):
        for city, info in self.data.items():
            for date, info_date in info.items():
                yield f"{city}:  {date} - {info_date}"
