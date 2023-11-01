n = int(input("Enter any Natural number: "))

def factorial(x):
    res = 1
    if x > 1:
        res = x * factorial(x-1)
    return res
# res = 6 * (5 * (4 * (3 * (2 * (1)))))
result = factorial(n)
print(result)