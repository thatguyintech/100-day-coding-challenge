def isMinHeap(arr):
    def subTreeIsHeap(index, arr, arraySize):
        if index >= arraySize:
            return True

        left, right = index*2 + 1, index*2 + 2
        leftBigger, rightBigger = True, True
        if left < arraySize:
            leftBigger = (arr[index] <= arr[left])
        if right < arraySize:
            rightBigger = (arr[index] <= arr[right])

        return leftBigger and rightBigger and subTreeIsHeap(left, arr, size) and subTreeIsHeap(right, arr, size)

    size = len(arr)
    return arr[0] <= arr[1] and arr[0] <= arr[2] and subTreeIsHeap(1, arr, size) and subTreeIsHeap(2, arr, size)
