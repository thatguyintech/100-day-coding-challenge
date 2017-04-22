def writeX(matrix):
    rows = set()
    cols = set()

    height = len(matrix[0])
    width = len(matrix)

    for i in xrange(height):
        for j in xrange(width):
            if matrix[i][j] == 'x':
                rows.add(i)
                cols.add(j)

    for row in rows:
        for j in xrange(width):
            if matrix[row][j] != 'x':
                matrix[row][j] = 'x'

    for i in xrange(height):
        for col in cols:
            if matrix[i][col] != 'x':
                matrix[i][col] = 'x'

    return matrix

def tests():
    t1 = [[]]
    o1 = [[]]
    assert(writeX(t1) == o1)

    t2 = [['x']]
    o2 = [['x']]
    assert(writeX(t2) == o2)

    t3 = [['-','-'],['-','x']]
    o3 = [['-','x'],['x','x']] 
    assert(writeX(t3) == o3)

    t4 = [['-','x'],['-','x']]
    o4 = [['x','x'],['x','x']]
    assert(writeX(t4) == o4)

    t5 = [['x','-'],['-','x']]
    o5 = [['x','x'],['x','x']]
    assert(writeX(t5) == o5)

    t6 = [['-','-','-','-','-'],['-','-','-','-','-'],['-','-','-','x','-'],['x','-','-','-','-'],['-','-','-','-','-']]
    o6 = [['x','-','-','x','-'],['x','-','-','x','-'],['x','x','x','x','x'],['x','x','x','x','x'],['x','-','-','x','-']]
    assert(writeX(t6) == o6)

tests()
