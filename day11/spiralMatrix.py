def spiralMatrixArr(matrix):
    return [1]

def tests():
    matrix = [[1,  2,  3,  4], [ 5,  6,  7,  8], [ 9,  10, 11, 12], [ 13, 14, 15, 16]]
    assert(spiralMatrixArr(matrix) == [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10])

tests()