a = sorted(list(map(int, input().split())), reverse = True)
print(a)
# list_1 = input().split() 
def negativeNumbers(a):
    b = []
    for i in a:
        if i < 0:
            b.append(abs(i))
    return b
if negativeNumbers(a):
    c = max(negativeNumbers(a))
    for i in range(1,c+2):
        if i not in negativeNumbers(a):
            print(i*(-1))
            break
else:
    print(-1)