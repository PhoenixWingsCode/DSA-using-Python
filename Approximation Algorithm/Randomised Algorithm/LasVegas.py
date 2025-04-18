import random

def las_vegas_max(arr):
    while True:
        # Randomly select an element from the list
        candidate = random.choice(arr)
        # Check if the candidate is the maximum element
        if all(candidate >= x for x in arr):
            return candidate

# Example usage
arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
max_element = las_vegas_max(arr)
print(f"The maximum element is: {max_element}")