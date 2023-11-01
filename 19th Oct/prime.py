num = int(input("Enter any number: "))
count = 0
for i in range(2,num):
    if num%i==0:
        count += 1
if num > 1:
    if count < 1:
        print("Given number is a prime")
    else:
        print("Given number is a consonant")
else:
    print("Enter a valid number")