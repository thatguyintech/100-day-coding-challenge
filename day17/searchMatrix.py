def searchMatrix(matrix, value):
    numRows, numCols = len(matrix), len(matrix[0])
    lowerBound, upperBound = 0, numRows * numCols - 1

    # empty matrix edge case
    if numCols == 0 or numRows == 0:
        return False

    # one item edge case
    if numCols == 1 and numRows == 1:
        return matrix[0][0] == value

    while lowerBound < upperBound:
        # translation
        middleIndex = (lowerBound + upperBound) / 2
        coordinate = indexToCoord(middleIndex, numCols)
        rowIndex, columnIndex = coordinate

        # get the value
        middleValue = matrix[rowIndex][columnIndex]

        if value == middleValue:
            return True
        elif value < middleValue:
            upperBound = middleIndex
        elif value > middleValue:
            lowerBound = middleIndex+1

    # first and last elements edge case
    endCoord = indexToCoord(lowerBound, numCols)
    if matrix[endCoord[0]][endCoord[1]] == value:
        return True

    return False

def indexToCoord(index, matrixWidth):
    return (index/matrixWidth, index%matrixWidth)

#########
# Tests #
#########

def testIndexToCoord():
    assert indexToCoord(21, 4) == (5, 1)
    assert indexToCoord(10, 4) == (2, 2)
    assert indexToCoord(4, 4) == (1, 0)
    assert indexToCoord(0, 4) == (0, 0)

def testSearchMatrix():
    assert not searchMatrix([[]], 0)
    assert searchMatrix([[1]], 1)
    assert searchMatrix([[1, 2, 3, 4, 5]], 4)
    assert searchMatrix([[1, 2, 3, 4, 5]], 5)
    assert not searchMatrix([[1, 2, 3, 4, 5]], 6)
    assert searchMatrix([[1],[2],[3],[4],[5]], 4)
    assert searchMatrix([[1],[2],[3],[4],[5]], 5)
    assert not searchMatrix([[1],[2],[3],[4],[5]], 6)

    t = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
    assert searchMatrix(t, 1)
    assert searchMatrix(t, 2)
    assert searchMatrix(t, 5)
    assert searchMatrix(t, 9)

def main():
    testIndexToCoord()
    testSearchMatrix()

if __name__ == "__main__":
    main()

