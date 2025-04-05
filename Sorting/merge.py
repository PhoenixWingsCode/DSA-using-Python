def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    #Create temporary arrays
    L = [0] * n1
    R = [0] * n2

    # Copy data to temporary arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    i = 0 # Initial index of first subarray
    j = 0 # Initial index of second subarray
    k = l # Initial index of merged subarray

    # Merge the temporary arrays back into arr[l..r ]
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def mergeSort(arr, l, r):
    if l < r:
        m = l + (r - l) //2

        #Sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)

# Example usage
arr = [12, 11, 13, 5, 6, 7]
print("Given array is")
print(arr)
mergeSort(arr, 0, len(arr) - 1)
print("\nSorted array is")
print(arr)       