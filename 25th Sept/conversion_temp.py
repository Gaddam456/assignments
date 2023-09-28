temp = float(input())
conversion = input()
if conversion == "C to F":
    print(temp*9/5 + 32)
elif conversion == "F to C":
    print((temp-32)*5/9)