def reverse_array(arr):
    left = 0
    right = len(arr) - 1
    
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    
    return arr


arr = list(map(int, input("Enter the array elements separated by spaces: ").split()))


print("Original array :", arr)

reversed_arr = reverse_array(arr)


print("Reversed array :", reversed_arr)