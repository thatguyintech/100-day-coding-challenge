def writeX(matrix):
    rowsToChange = set()
    colsToChange = set()

    height = len(matrix[0])
    width = len(matrix)

    for i in xrange(height):
        for j in xrange(width):
            if matrix[i][j] == 'x':
                rowsToChange.add(i)
                colsToChange.add(j)

    for row in rowsToChange:
        for j in xrange(width):
            if matrix[row][j] != 'x':
                matrix[row][j] = 'x'

    for i in xrange(height):
        for col in colsToChange:
            if matrix[i][col] != 'x':
                matrix[i][col] = 'x'

    return matrix

def tests():

    # empty matrix
    t1 = [[]]
    o1 = [[]]
    assert writeX(t1) == o1

    # small matrix
    t2 = [['x']]
    o2 = [['x']]
    assert writeX(t2) == o2

    # simple matrix, one x
    t3 = [['-','-'],
          ['-','x']]

    o3 = [['-','x'],
          ['x','x']] 
    assert writeX(t3) == o3

    # simple matrix, overlapping x's
    t4 = [['-','x'],
          ['-','x']]

    o4 = [['x','x'],
          ['x','x']]
    assert writeX(t4) == o4

    # simple matrix, multiple overlaps
    t5 = [['x','-'],['-','x']]
    o5 = [['x','x'],['x','x']]
    assert writeX(t5) == o5

    # big matrix
    t6 = [['-','-','-','-','-'],
          ['-','-','-','-','-'],
          ['-','-','-','x','-'],
          ['x','-','-','-','-'],
          ['-','-','-','-','-']]

    o6 = [['x','-','-','x','-'],
          ['x','-','-','x','-'],
          ['x','x','x','x','x'],
          ['x','x','x','x','x'],
          ['x','-','-','x','-']]
    assert writeX(t6) == o6

tests()
