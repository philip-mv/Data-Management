def subarraysum(arr,n,sum_):
    for i in range(n):
        curr_sum = arr[i]
        j = i + 1
        while j <=n:

            if curr_sum == sum_:
                 print("Sum found Between")
                 print("indexes %d and %d"%(i,j-1))
                 return 1
            if curr_sum > sum_ or j == n :
                break
            curr_sum = curr_sum +arr[j]
            j += 1
    print ("No subaray found")
    return 0 
arr = [15,2,4,8,9,5,10,23]
n = len(arr)
sum_ = 23
subarraysum(arr,n,sum_)