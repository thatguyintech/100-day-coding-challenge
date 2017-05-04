def searchMatrix(matrix, target)
  # the downside to this is that I do a binary search
  # on every row before I return
  matrix.map {|row| binarySearch(row, target)}.any? {|result| result == true}
end

###########
# Helpers #
###########

def binarySearch(row, target)
  low, high = 0, row.size

  while low < high  
    mid = (low + high) / 2
    if row[mid] == target
      return true
    elsif target > row[mid]
      low = mid + 1
    else
      high = mid
    end
  end

  false
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
  matrix = [[1,2,3],
            [4,5,6],
            [7,8,9]]
  assert { searchMatrix(matrix, 1) }
  assert { searchMatrix(matrix, 2) }
  assert { searchMatrix(matrix, 5) }
  assert { searchMatrix(matrix, 6) }
  assert { searchMatrix(matrix, 8) }
  assert { searchMatrix(matrix, 9) }

  assert { searchMatrix([[]], 0) == false }
  assert { searchMatrix([[0]], 1) == false }
  assert { searchMatrix([[1, 2]], 0) == false }
  assert { searchMatrix([[1],[2],[3]], 0) == false }
  assert { searchMatrix([[1],[2],[3]], 1) == true }
  assert { searchMatrix([[1],[2],[3]], 3) == true }
end

tests()