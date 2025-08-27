def max_difference(arr):
    if len(arr) < 2:
        return 0
    min_num = arr[0]
    max_num = arr[0]
    for num in arr:
        min_num = min(min_num, num)
        max_num = max(max_num, num)
    return max_num - min_num


arr = list(map(int, input("Enter the array elements separated by spaces: ").split()))


print("Output :", max_difference(arr))