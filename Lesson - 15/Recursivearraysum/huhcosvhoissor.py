def arrayTotalSum(a):
    length = len(a)
    if length == 1 :
        return a[0]
    return a[0] + arrayTotalSum(a[1:])
a = [1,2,3,6]
print("array total sum:", arrayTotalSum(a))