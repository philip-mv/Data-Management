number_largest = int(input("Please enter the larger number :" ))
number_smallest = int(input("Please enter the smallest number :" ))
while number_smallest:
    number_store = number_smallest
    number_smallest = number_largest % number_smallest
    number_largest = number_store
print("HCF = ",number_largest)