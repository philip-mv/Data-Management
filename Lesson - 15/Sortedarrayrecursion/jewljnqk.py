def checkSorted(a):
    length = len(a)
    if length == 1 or length == 0:
        return True
    return a[0] <= a[1] and checkSorted(a[1:])
a = [1,2,3,4,5,6,8,2]
if checkSorted(a):
    print("Yes given array is sorted")
else:
    print("NO given array is not sorted 🥲")