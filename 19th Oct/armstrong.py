numbStr = input("Enter any number: ")
length_num = len(numbStr)
s = 0
for i in numbStr:
    s += int(i) ** length_num
if s == int(numbStr):
    print("Given number is an Armstrong Number")
else:
    print("Given number is not an Armstrong number")