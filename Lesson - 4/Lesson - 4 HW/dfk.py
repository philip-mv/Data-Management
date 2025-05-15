def binary_to_decimal(binary_num):

    decimal_num = 0
    power = 0

    
    for digit in reversed(binary_num):
        if digit == '1':
            decimal_num += 2 ** power  
        elif digit != '0':
            return 0
        power += 1 
    return decimal_num

if __name__ == "__main__":
    while True:
        binary_input = input("Enter a binary number (or 'q' to quit): ")
        if binary_input.lower() == 'q':
            break
        decimal_output = binary_to_decimal(binary_input)

        if decimal_output == 0:
            print("Invalid binary number. Please enter a number containing only 0s and 1s.")
        else:
            print(f"Decimal: {decimal_output}")
