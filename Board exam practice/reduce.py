from functools import reduce

number = [1,2,3,4]
result = reduce(lambda x,y:x+y, number)
print(result)