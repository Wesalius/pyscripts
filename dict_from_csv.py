import csv


file_list = [","]

def create_dict_from_csv(input_csv_file):
    with open(input_csv_file, "r", encoding="utf-8") as fide_csv_rating_file:
        rating_dictionary = dict(csv.reader(fide_csv_rating_file))

for file in file_list:
    create_dict_from_csv(file)