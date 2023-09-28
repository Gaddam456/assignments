age = int(input("Enter your age: "))
if age >= 0 and age <= 12:
    print("You are a Child.")
elif age >= 13 and age <= 19:
    print("You are a Teenager.")
elif age >= 20 and age <= 59:
    print("You are an Adult.")
elif age >= 60:
    print("You are a Senior citizen.")
else:
    print("Enter a valid age!")