import csv

file_path = input("Enter the path of the CSV file: ")

try:
    with open(file_path, newline='') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            print(row)
except FileNotFoundError:
    print(f"The file at {file_path} does not exist.")
