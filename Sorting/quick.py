# Function to find the partition position
def partition(array, low, high):
    pivot = array[high] # choose the rightmost element as pivot
    i = low - 1 # pointer for the greater element

    # traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1 # if element smaller than pivot is found
            array[i], array[j] = array[j], array[i] # swap it with the greater element pointed by i

    array[i + 1], array[high] = array[high], array[i + 1] # swap the pivot element with the greater element specified by i
    return i + 1 # return the position from where partition is done

# function to perform quicksort
def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high) # find pivot element such that element smaller than pivot are on the left and element greater than pivot are on the right
        quickSort(array, low, pi - 1) # recursive call on the left of pivot
        quickSort(array, pi + 1, high) # recursive call on the right of pivot
        
# Example usage
data = [1, 7, 4, 1, 10, 9, -2]
print("Unsorted Array")
print(data)
size = len(data)
quickSort(data, 0, size - 1)
print('Sorted Array in Ascending Order:')
print(data)