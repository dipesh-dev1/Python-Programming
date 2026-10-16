import re

text = "I have 2 books and 18 pens."

numbers = re.findall(r"\d+", text)

print(numbers)