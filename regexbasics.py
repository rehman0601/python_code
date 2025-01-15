import re

# Sample string containing email addresses
text = "Contact us at support@example.com or sales@example.org for more info."

# Regular expression to extract email addresses
emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)

# Print the extracted email addresses
print("Extracted email addresses:", emails)
