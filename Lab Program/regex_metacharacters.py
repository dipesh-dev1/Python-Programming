import re

print(re.findall(r'a.c', "abc axc"))
print(re.findall(r'^Hello', "Hello Python"))
print(re.findall(r'Python$', "I love Python"))
print(re.findall(r'ab*', "a ab abb"))
print(re.findall(r'ab+', "ab abb abbb"))