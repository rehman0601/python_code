import json

# Read JSON data from a file
with open('data.json', 'r') as file:
    data = json.load(file)

# Modify a value
data['name'] = 'John Doe'

# Write updated data back to the file
with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)

print("Updated data written to data.json")
