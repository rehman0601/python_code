import json

def read_and_modify_json(file_path):
    try:
        # Read the JSON file
        with open(file_path, 'r') as file:
            data = json.load(file)

        # Modify the JSON data
        print(f"Original data: {data}")
        data['key'] = 'new_value'  # Modify the value of 'key'

        # Write the modified data back to the JSON file
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)

        print(f"Modified data has been written back to {file_path}.")
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
    except json.JSONDecodeError:
        print(f"Error: The file {file_path} is not a valid JSON file.")

# Test the function
file_path = input("Enter the JSON file path: ")
read_and_modify_json(file_path)
