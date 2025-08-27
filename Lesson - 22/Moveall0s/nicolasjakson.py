def pushZerosToEnd(a,a_size):
    zero = 0
    nonzero = 0
    while(nonzero!=a_size):
        if a[nonzero]!=0:
            a[nonzero],a[zero] = a[zero],a[nonzero]
            zero+=1
        nonzero+=1
a = [0,-1,-0,72,-2]
a_size = len(a)
print(a)
pushZerosToEnd(a,a_size)
print("Array after pushing all zeros to end of array :")
print(a)