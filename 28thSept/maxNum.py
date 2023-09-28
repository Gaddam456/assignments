list_a = [43, 88, 72, 21, 56]

def maxNum(a):
    res = a[0]
    for i in range(1,len(a)):
        if res < a[i]:
            res = a[i]
    print(res)

maxNum(list_a)