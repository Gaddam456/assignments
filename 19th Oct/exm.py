list_a = input().split()
for i in range(len(list_a)):
    list_a[i] = int(list_a[i])
print(list_a)

list_b = list(map(str, list_a))
print(list_b)

list_c = list(map(int, list_b))
print(list_c)