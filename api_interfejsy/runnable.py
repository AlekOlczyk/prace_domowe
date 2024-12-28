from file_handler import FileHandler

file_handler = FileHandler("date_data.json")

file_handler["Krakow", "2024-11-27"] = "Nie pada"
print(file_handler.data)

print(file_handler["Wroclaw", "2024-11-27"])

for info in file_handler:
    print(info)

generator = file_handler.items()

for info in generator:
    print(info)