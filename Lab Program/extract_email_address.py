import re

text = "Contact us at chaudharydipesh190@gmail.com or sita@yahoo.com"

emails = re.findall(r'\S+@\S+\.\S+', text)

print(emails)