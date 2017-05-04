########
# Code #
########

# pattern and matrix are both 2D arrays
# return true as soon as the pattern is found for a first time
def patternInMatrix(pattern, matrix):
    rows, cols = len(matrix), len(matrix[0])
    patternRows, patternCols = len(pattern), len(pattern[0])
    for row in xrange(rows-patternRows):
        for col in xrange(cols-patternCols):
            found = False
            for pRow in xrange(patternRows):
                for pCol in xrange(patternCols):
                    if pattern[pRow][pCol] != matrix[row+pRow][col+pCol]:
                        found = False
                        break
                    else:
                        found = True
            if found:
                return True
    return False

# return a list of all top-left starting indices
def indicesOfPatternInMatrix(pattern, matrix):
    rows, cols = len(matrix), len(matrix[0])
    patternRows, patternCols = len(pattern), len(pattern[0])

    startingSpots = []
    for row in xrange(rows-patternRows+1):
        for col in xrange(cols-patternCols+1):
            found = False
            for pRow in xrange(patternRows):
                for pCol in xrange(patternCols):
                    if pattern[pRow][pCol] != matrix[row+pRow][col+pCol]:
                        found = False
                        break
                    else:
                        found = True
            if found:
                startingSpots.append((row, col))
    return startingSpots

#########
# Tests #
#########

def testPatterInMatrix():
    assert patternInMatrix([[1]], [[0,0,0],[0,1,0],[0,0,0]])
    assert not patternInMatrix([[2]], [[0,0,0],[0,1,0],[0,0,0]])

def testIndicesOfPatternInMatrix():
    p0 = [[1]]

    m0 = [[0,0,0],
          [0,1,0],
          [0,0,0]]
    assert indicesOfPatternInMatrix(p0, m0) == [(1, 1)]

    p1 = [[2]]

    m1 = [[0,0,0],
          [0,1,0],
          [0,0,0]]
    assert indicesOfPatternInMatrix(p1, m1) == []

    p2 = [[0,1,0]]

    m2 = [[0,0,0],
          [0,1,0],
          [0,0,0]]
    assert indicesOfPatternInMatrix(p2, m2) == [(1, 0)]

    p3 = [[0,0,0],
          [0,1,0],
          [0,0,0]] 

    m3 = [[0,0,0],
          [0,1,0],
          [0,0,0]] 
    assert indicesOfPatternInMatrix(p3, m3) == [(0,0)]

    p4 = [[0]]

    m4 = [[0,0,0],
          [0,1,0],
          [0,0,0]] 
    assert indicesOfPatternInMatrix(p4, m4) == [(0,0),(0,1),(0,2),
                                                (1,0),(1,2),
                                                (2,0),(2,1),(2,2)]

    p4 = [[0, 0]]

    m4 = [[0,0,0],
          [0,1,0],
          [0,0,0]] 
    assert indicesOfPatternInMatrix(p4, m4) == [(0,0),(0,1),
                                                (2,0),(2,1)]

def main():
    testPatterInMatrix()
    testIndicesOfPatternInMatrix()

if __name__ == "__main__":
    main()