# returns the sums of values located at the coordinates denoted
# by the rectangle enclosed by the top left coordinate `topLeft`
# and the bottom right coordinate `bottomRight` inside `matrix`.
def rectangleSum(sumsMatrix, topLeft, bottomRight):
    if sumsMatrix == [[]]:
        return 0

    # x index denotes row in the matrix
    # y index denotes column in the matrix
    topLeftX, topLeftY = topLeft
    bottomRightX, bottomRightY = bottomRight

    # negative rectangle, default to 0
    if topLeftX < bottomRightX or topLeftY > bottomRightY:
        return 0

    # bigRectSum is the sum of the rectangle formed by the 
    # origin and the bottom right coordinate
    bigRectSum = sumsMatrix[bottomRightX][bottomRight]

    # we're done if the top left coordinate is the origin
    if topLeftX == 0 and topLeftY == 0:
        return bigRectSum 

    # default the rect sums to 0 in case of borders
    leftRectSum = 0
    if topLeftY > 0:
        leftRectSum = sumsMatrix[bottomRightX][topLeftY-1]

    topRectSum = 0
    if topLeftX > 0:
        topRectSum = sumsMatrix[topLeftX-1][bottomRightY]

    cornerRectSum = 0
    if topLeftX > 0 and topLeftY > 0:
        cornerRectSum = sumsMatrix[topLeftX-1][topLeftY-1]

    return bigRectSum + cornerRectSum - leftRectSum - topRectSum

# performs preprocessing on a matrix to cache relevant sums
def cacheSums(matrix):
    rows, cols = len(matrix), len(matrix[0])

    if rows == 0 or cols == 0:
        return [[]]

    sumsMatrix = [[0 for col in xrange(cols)] for row in xrange(rows)]

    sumsMatrix[0][0] = matrix[0][0]

    for row in xrange(1, rows):
        sumsMatrix[row][0] = sumsMatrix[row-1][0] + matrix[row][0]
    for col in xrange(1, cols):
        sumsMatrix[0][col] = sumsMatrix[0][col-1] + matrix[0][col]

    for row in xrange(1, rows):
        for col in xrange(1, cols):
            leftRectSum = sumsMatrix[row][col-1]
            topRectSum = sumsMatrix[row-1][col]
            cornerRectSum = sumsMatrix[row-1][col-1]
            sumsMatrix[row][col] = matrix[row][col] + leftRectSum + topRectSum - cornerRectSum

    return sumsMatrix

#########
# Tests #
#########

def testCacheSums():
    t0 = [[1,2,3],
          [1,2,3],
          [1,2,3]]
    r0 = [[1,3,6],
          [2,6,12],
          [3,9,18]]
    assert cacheSums(t0) == r0

    t1 = [[]]
    r1 = [[]]
    assert cacheSums(t1) == r1

    t2 = [[1,2,3]]
    r2 = [[1,3,6]]
    assert cacheSums(t2) == r2

    t3 = [[0]]
    r3 = [[0]]
    assert cacheSums(t3) == r3

    t4 = [[0],
          [1],
          [2],
          [3]]
    r4 = [[0],
          [1],
          [3],
          [6]]
    assert cacheSums(t4) == r4

def testRectangleSum():
    matrix = [[1,2,3],
              [1,2,3],
              [1,2,3]]
    sumsMatrix = cacheSums(matrix)

    l0 = (0,0)
    r0 = (0,0)
    assert rectangleSum(sumsMatrix, l0, r0) == 0

    l1 = (0,0)
    r1 = (-1,0)
    assert rectangleSum(sumsMatrix, l1, r1) == 0

    l2 = (0,0)
    r2 = (1,1)
    assert rectangleSum(sumsMatrix, l2, r2) == 6

    l3 = (0,0)
    r3 = (1,2)
    assert rectangleSum(sumsMatrix, l3, r3) == 12

    l4 = (0,0)
    r4 = (2,1)
    assert rectangleSum(sumsMatrix, l4, r4) == 9

    l5 = (1,1)
    r5 = (2,2)
    assert rectangleSum(sumsMatrix, l3, r3) == 18

def main():
    testCacheSums()

if __name__ == "__main__":
    main()
    