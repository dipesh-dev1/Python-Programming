import re

text = "My phone number is 984-123-4567 and my age is 20."

# Replace phone number with AWESOME
text = re.sub(r'\d{3}-\d{3}-\d{4}', 'AWESOME', text)

# Replace all remaining digits with #
text = re.sub(r'\d', '#', text)

print(text)