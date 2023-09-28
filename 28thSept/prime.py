def prime_func(p):
    res = "Given number is a Prime"
    for i in range(2,p):
        if p % i != 0:
            continue
        else:
            res = "Given number is not a Prime"
            break
    return res



num = int(input("Enter any Natural number: "))
result = prime_func(num)
print(result)