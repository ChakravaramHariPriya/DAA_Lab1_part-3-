def segregate_zeros_ones(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        if arr[left] == 0 and arr[right] == 1:
            left += 1
            right -= 1
        elif arr[left] == 0:
            left += 1
        elif arr[right] == 1:
            right -= 1

    for i in range(left, len(arr)):
        arr[i] = 1

arr = [0, 1, 0, 1, 0, 0, 1, 1, 1, 0]
segregate_zeros_ones(arr)
print(arr)

arr = [1, 1, 1, 1, 1, 0, 0, 0, 0]
segregate_zeros_ones(arr)
print(arr)

arr = [1, 0, 0, 1, 1, 0, 1, 1, 1, 1]
segregate_zeros_ones(arr)
print(arr)  
