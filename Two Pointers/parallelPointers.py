# Find if there is a pair with sum = target in a sorted list
def has_pair_with_sum(arr, target):
    left, right = 0, len(arr) - 1  # Two pointers
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return True
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return False

arr = [1, 2, 3, 4, 6]
print(has_pair_with_sum(arr, 10))  # True (4 + 6)