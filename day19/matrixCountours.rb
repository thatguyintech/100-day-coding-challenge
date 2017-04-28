def countourDistances(matrix)
  matrix
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
  assert { countourDistances(empty) == emptyOutput }

  one = [[0]]
  oneOutput = [[0]]
  assert { countourDistances(one) == oneOutput }

  # other cases
  matrix = [[1,1,1],
            [1,0,1],
            [1,1,1]]

  output = [[2,1,2],
            [1,0,1],
            [2,1,2]]
  assert { countourDistances(matrix) == output }

  matrix1 = [[0,0,0],
             [0,1,0],
             [0,0,0]]

  output1 = [[0,0,0],
             [0,1,0],
             [0,0,0]]
  assert { countourDistances(matrix1) == output1 }

  matrix2 = [[0,0,0],
             [0,1,0],
             [1,1,1]]
             
  output2 = [[0,0,0],
             [0,1,0],
             [1,2,1]]
  assert { countourDistances(matrix2) == output2 }
end

tests()