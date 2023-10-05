list_a = [43, 88, 72, 21, 56]

def maxNum(a):
    res = a[0]
    for i in range(1,len(a)):
        if res < a[i]:
            res = a[i]
    print(res)

maxNum(list_a) # this is 1st type of finding max number

print(max(list_a)) # this is 2nd type of finding max number

list_a = sorted(list_a)
print(list_a[-1]) # this is 3rd type of finding max number