def myfunction1(n):
   
    if(n>0):
        return
    for i in range (0,n+1):
        print("Codingal")
    myfunction1(n/2)
    myfunction1(n/3)

def myfunction2(n):
   
    if(n<=1):
        return
    print("Codingal")
    myfunction2(n-1)

def analyze_time_complexity():
    
    print("Recurrence relation for myfunction1(n):")
    print("T(n) = T(n/2) + T(n/3) + O(n)  for n > 0")
    print("T(n) = O(1)                   for n <= 0")
    print()
    print("Time complexity of myfunction1(n): Approximately O(n^1.39)")
    print()
    print("Recurrence relation for myfunction2(n):")
    print("T(n) = T(n-1) + O(1)  for n > 1")
    print("T(n) = O(1)           for n <= 1")
    print()
    print("Time complexity of myfunction2(n): O(n)")

if __name__ == "__main__":
    analyze_time_complexity()

    