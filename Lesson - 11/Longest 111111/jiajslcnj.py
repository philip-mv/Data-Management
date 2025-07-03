def longest_consecutive_ones(number):

    if number <= 0:
        return 0

    max_length = 0
    current_length = 0


    while number > 0:
    
        if (number & 1) == 1:
            current_length += 1
        else:
        
            current_length = 0



    
        max_length = max(max_length, current_length)

    

        number >>= 1

    return max_length

try:

    user_number = int(input("Enter your number: "))


    length = longest_consecutive_ones(user_number)


    print(f"Longest consecutive 1's length: {length}")

except ValueError:

    print("Invalid input. Please enter a valid integer.")



