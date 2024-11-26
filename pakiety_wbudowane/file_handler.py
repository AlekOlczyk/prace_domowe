import csv


class FileHandler:
    def __init__(self, input_file, output_file, transformations):
        self.input_file = input_file
        self.output_file = output_file
        self.transformations = transformations
        self.matrix = self.load_data_from_input_file()
        print(self.transformations)

    def load_data_from_input_file(self):
        temp_matrix = []
        with open(self.input_file) as file:
            reader = csv.reader(file)
            for row in reader:
                temp_matrix.append(row)
        return temp_matrix

    def save_data_to_output_file(self):
        with open(self.output_file, mode="w") as file:
            writer = csv.writer(file)
            for line in self.matrix:
                writer.writerow(line)

    def transform(self):
        for transformation in self.transformations:
            transformation_list = transformation.split(",")
            print(transformation_list)
