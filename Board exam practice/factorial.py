def factiorial(n):
    if n == 0:
        return 1
    return n * factiorial(n-1)

a = int(input("Enter a number:"))
print(factiorial(a))