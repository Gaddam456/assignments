integer = int(input("Enter any natural number: "))
if integer > 0:
    string1 = str(integer)
    print(string1[::-1])
else:
    print("Enter a valid number")