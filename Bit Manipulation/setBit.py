def set_bit(N, i):
    mask = 1 << i  # Create a mask by shifting 1 left by i positions
    return N | mask  # Use bitwise OR to set the ith bit

number = 5  # Binary: 0101
position = 1  # We want to set the 1st bit

new_number = set_bit(number, position)
print(bin(new_number))  # Output: 0b111 (Decimal: 7)