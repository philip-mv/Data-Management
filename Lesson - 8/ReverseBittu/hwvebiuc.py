def reverse_bits(n):
    """
    Reverses the bits of a given non-negative integer.
    Assumes reversal based on the number of bits actually used by 'n'.
    """
    reversed_num = 0
    # Determine the number of bits to consider based on the input number's length
    # If n is 0, bit_length() is 0, so handle it to ensure at least 1 bit (for "0")
    num_bits = n.bit_length() if n > 0 else 1

    temp_n = n
    for _ in range(num_bits):
        reversed_num <<= 1          # Shift reversed_num left to make space
        reversed_num |= (temp_n & 1) # Add the least significant bit of temp_n
        temp_n >>= 1                # Shift temp_n right to process next bit
    return reversed_num

def to_binary_string(n, min_bits=0):
    """Converts an integer to its binary string representation with optional padding."""
    if n == 0:
        return "0" * max(1, min_bits)
    binary = bin(n)[2:]
    return binary.zfill(max(len(binary), min_bits))

def main():
    try:
        original_number = int(input("Enter your original number: "))

        if original_number < 0:
            print("Please enter a non-negative integer.")
            return

        
        bit_length_for_display = original_number.bit_length() if original_number > 0 else 1

        reversed_val = reverse_bits(original_number)

        original_binary_str = to_binary_string(original_number, bit_length_for_display)
        reversed_binary_str = to_binary_string(reversed_val, bit_length_for_display)

        print(f"Original Number : {original_number} ({original_binary_str})")
        print(f"Reversed Number : {reversed_val} ({reversed_binary_str})")

    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()