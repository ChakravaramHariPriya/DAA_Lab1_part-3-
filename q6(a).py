def find_sum_pair(arr, K):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == K:
                return True, (arr[i], arr[j])
    return False, None


arr = [8, 4, 1, 6]
K = 10
found, pair = find_sum_pair(arr, K)
if found:
    print(f"Yes, the pair is {pair}")
else:
    print("No pair found")
