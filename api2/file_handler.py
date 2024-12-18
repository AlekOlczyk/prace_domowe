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
