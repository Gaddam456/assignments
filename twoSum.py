list_a = [4,5,6,7,8,10,11]
target = 18
left = 0
right = len(list_a) - 1
while left < right:
    if list_a[left] + list_a[right] == target:
        print([left, right])
    left = left + 1
    if left == right:
        left = 0
        right = right - 1