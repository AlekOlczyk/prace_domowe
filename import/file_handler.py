import json


class FileHandler:
    def __init__(self, data_file, history_file):
        self.data_file = data_file
        self.history_file = history_file

    def load_data_from_data_file(self):
        with open(self.data_file) as file:
            return json.loads(file.read())

    def load_data_from_history_file(self):
        with open(self.history_file) as file:
            return json.loads(file.read())

    def save_data_to_data_file(self, balance, stock):
        with open(self.data_file, mode="w") as file:
            file.write(json.dumps({
                "saldo": balance,
                "stan_magazynowy": stock
            }))

    def save_history_to_history_file(self, history):
        with open(self.history_file, mode="w") as file:     #czemu w, wedlug mnie a
            file.write(json.dumps(history))
