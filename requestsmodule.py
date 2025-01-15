import requests

# Fetch data from a public API (example: JSONPlaceholder)
response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
data = response.json()

# Print part of the JSON response
print(f"User ID: {data['userId']}")
print(f"Title: {data['title']}")
