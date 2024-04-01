def merge(arr, temp_arr, left, mid, right):
    i = left  
    j = mid + 1  
    k = left  
    inversion_count = 0

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            i += 1
        else:
            temp_arr[k] = arr[j]
            j += 1
            inversion_count += (mid - i + 1) 

        k += 1

    while i <= mid:
        temp_arr[k] = arr[i]
        i += 1
        k += 1

    while j <= right:
        temp_arr[k] = arr[j]
        j += 1
        k += 1

    for loop_var in range(left, right + 1):
        arr[loop_var] = temp_arr[loop_var]

    return inversion_count

def merge_sort(arr, temp_arr, left, right):
    inversion_count = 0
    if left < right:
        mid = (left + right) // 2
        inversion_count += merge_sort(arr, temp_arr, left, mid)
        inversion_count += merge_sort(arr, temp_arr, mid + 1, right)
        inversion_count += merge(arr, temp_arr, left, mid, right)

    return inversion_count

def inversion_count(arr):
    n = len(arr)
    temp_arr = [0] * n
    return merge_sort(arr, temp_arr, 0, n - 1)

# Example usage
arr = [10, 1, 2, 4, 13, 9, 5]
print("Number of inversions:", inversion_count(arr))
