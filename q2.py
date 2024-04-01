def find_max_product_pair(arr):
    arr.sort()
    n = len(arr)
    max_product = arr[n-1] * arr[n-2]
    return arr[n-1], arr[n-2], max_product

# Example usage
arr = [1, 7, 4, 2, 8, 6, 3, 9, 5]
num1, num2, max_product = find_max_product_pair(arr)
print(f"The pair with maximum product is ({num1}, {num2}) with product {max_product}")
