def find_missing_number(arr):
    n = len(arr) + 1  
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    missing_number = expected_sum - actual_sum
    return missing_number

arr = list(map(int, input("Enter the array elements separated by spaces: ").split()))


print("output =", find_missing_number(arr))