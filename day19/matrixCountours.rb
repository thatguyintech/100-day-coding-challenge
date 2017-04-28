def contourDistances(matrix)
  rows, cols = matrix.size, matrix[0].size

  if rows == 0 || cols == 0
    return matrix
  end

  contours = Array.new(rows).map { |x| [nil] * cols }
  queue = []
  # start by finding 0s
  for row in 0..rows-1
    for col in 0..cols-1
      if matrix[row][col] == 0
        queue << [row, col]
        contours[row][col] = 0
      end
    end
  end

  # do bfs
  while queue.size > 0
    current = queue.shift
    row, col = current
    contours[row][col] = getMinNeighbor(contours, row, col) + 1
    for i, j in [[row-1, col], [row, col-1], [row, col+1], [row+1, col]]
      if withinBounds([i, j], rows, cols) && contours[i][j] == nil
        queue << [i, j]
      end
    end
  end

  contours
end

def withinBounds(coordinate, rows, cols)
  x, y = coordinate
  x >= 0 && x < rows && y >= 0 && y < cols
end

def getMinNeighbor(matrix, row, col)
  if matrix[row][col] == 0
    return -1
  end

  vals = []
  rows, cols = matrix.size, matrix[0].size
  for i, j in [[row-1, col], [row, col-1], [row, col+1], [row+1, col]]
    if withinBounds([i, j], rows, cols)
      if matrix[i][j] != nil
        vals << matrix[i][j]
      end
    end
  end

  vals.min
end

#########
# Tests #
#########

class AssertionError < RuntimeError
end

def assert &block
  raise AssertionError unless yield
end

def tests
  # edge cases
  empty = [[]]
  emptyOutput = [[]]
  assert { contourDistances(empty) == emptyOutput }

  one = [[0]]
  oneOutput = [[0]]
  assert { contourDistances(one) == oneOutput }

  # other cases
  matrix = [[1,1,1],
            [1,0,1],
            [1,1,1]]

  output = [[2,1,2],
            [1,0,1],
            [2,1,2]]
  assert { contourDistances(matrix) == output }

  matrix1 = [[0,0,0],
             [0,1,0],
             [0,0,0]]

  output1 = [[0,0,0],
             [0,1,0],
             [0,0,0]]
  assert { contourDistances(matrix1) == output1 }

  matrix2 = [[0,0,0],
             [0,1,0],
             [1,1,1]]
             
  output2 = [[0,0,0],
             [0,1,0],
             [1,2,1]]
  assert { contourDistances(matrix2) == output2 }
end

tests()
