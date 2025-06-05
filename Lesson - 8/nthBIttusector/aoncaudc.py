def setOrNOt(numebr,n):
    mask = 1
    if (n & mask) == 1 or (n & mask) == 0:
        if numebr & (1 <<(n-1)):
            print("SET")
        else:
            print("NOT SET")
numebr = int(input("Enter the number:"))
n = int(input("Enter the  bit position :"))
setOrNOt(numebr,n)


