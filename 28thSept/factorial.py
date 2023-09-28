n = int(input("Enter any Natural number: "))

def factorial(x):
    res = 1
    if x > 1:
        res = x * factorial(x-1)
        return res
    else:
        return res

result = factorial(n)
print(result)