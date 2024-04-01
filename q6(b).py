def find_sum_pair(arr, K):
    arr.sort()
    left = 0
    right = len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == K:
            return True, (arr[left], arr[right])
        elif current_sum < K:
            left += 1
        else:
            right -= 1
    return False, None


arr = [8, 4, 1, 6]
K = 10
found, pair = find_sum_pair(arr, K)
if found:
    print(f"Yes, the pair is {pair}")
else:
    print("No pair found")
