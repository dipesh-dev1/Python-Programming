import re

text = "Python is easy language. Python is useful."

print(re.match("Python",text))
print(re.search("easy",text))
print(re.findall("is",text))
print(re.sub("Python", "Java",text))