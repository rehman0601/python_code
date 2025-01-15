import datetime

# Get current date and time
current_datetime = datetime.datetime.now()

# Format the datetime object
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
print(f"Current date and time: {formatted_datetime}")
