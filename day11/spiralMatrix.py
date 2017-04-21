def spiralMatrixArr(matrix):
    direction = 0

    # boundaries
    top, left = 0, 0
    right = len(matrix[0]) # row/width
    bottom = len(matrix) # column/height

    # starting coordinates
    row, col = 0, 0

    # for testing
    ret = []

    while top < bottom and left < right:
        # go right
        while col < right:
            ret.append(matrix[row][col])
            col += 1
        top += 1
        col -= 1

        # go down
        row += 1
        while row < bottom:
            ret.append(matrix[row][col])
            row += 1
        right -= 1
        row -= 1

        # go left
        col -= 1
        while col >= left and top < bottom:
            ret.append(matrix[row][col])
            col -= 1
        bottom -= 1
        col += 1

        # go up
        row -= 1
        while row >= top and left < right:
            ret.append(matrix[row][col])
            row -= 1
        row += 1
        left += 1
        
        col += 1
    return ret

def tests():
    matrix = [[1,  2,  3,  4], [ 5,  6,  7,  8], [ 9,  10, 11, 12], [ 13, 14, 15, 16]]
    assert(spiralMatrixArr(matrix) == [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10])
    assert(spiralMatrixArr([[]]) == [])
    assert(spiralMatrixArr([[1,2]]) == [1, 2])
    assert(spiralMatrixArr([[1],[2],[3],[4]]) == [1, 2, 3, 4])
    assert(spiralMatrixArr([[1,2],[8,3],[7,4],[6,5]]) == [1,2,3,4,5,6,7,8])

tests()