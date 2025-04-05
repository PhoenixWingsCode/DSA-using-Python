def selectionSort(arr):

    size = len(arr)

    for i in range(size):
        minIndex = i

        for j in range(i + 1, size):
            if arr[j] < arr[minIndex]:
                minIndex = j
            arr[i],arr[minIndex] = arr[minIndex],arr[i]

arr = [-2, 45, 0, 11, -9, 88, -97, -202, 747]
selectionSort(arr)
print('The array after sorting in Ascending Order by selection sort is:')
print(arr)