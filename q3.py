def sort_almost_sorted(arr):
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            start = 0
            end = i - 1
            while start < end:
                mid = (start + end) // 2
                if arr[mid] > arr[i]:
                    end = mid
                else:
                    start = mid + 1
            arr[start], arr[i] = arr[i], arr[start]

            for j in range(i+1, len(arr)):
                if arr[j] < arr[j-1]:
                    arr[j], arr[j-1] = arr[j-1], arr[j]
            break

arr = [3, 8, 6, 7, 5, 9]
sort_almost_sorted(arr)
print(arr)

arr = [3, 5, 6, 9, 8, 7]
sort_almost_sorted(arr)
print(arr)

arr = [3, 5, 7, 6, 8, 9]
sort_almost_sorted(arr)
print(arr)  
