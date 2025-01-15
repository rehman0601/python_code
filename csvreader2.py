import csv

def read_csv(file_path):
    try:
        with open(file_path, newline='') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                print(row)
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
    except IOError as e:
        print(f"Error: An IO error occurred. {e}")

# Test the function
file_path = input("Enter the CSV file path to read: ")
read_csv(file_path)
