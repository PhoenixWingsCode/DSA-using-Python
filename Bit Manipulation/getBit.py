def get_bit(N, i):
    return (N & (1 << i))!= 0

# Example usage
number = 5  # Binary representation: 101
position = 3
if get_bit(number, position):
    print("bit was one")
else:
    print("bit was zero")