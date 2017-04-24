# pattern and matrix are both 2D arrays
# return true if the pattern exists in the matrix
def patternInMatrix(pattern, matrix):
    pass

def indicesOfPatternInMatrix(pattern, matrix):
    pass

def main():
    assert patternInMatrix([[1]], [[0,0,0],[0,1,0],[0,0,0]])
    assert not patternInMatrix([[2]], [[0,0,0],[0,1,0],[0,0,0]])
    assert indicesOfPatternInMatrix([[1]], [[0,0,0],[0,1,0],[0,0,0]]) == [(1,1)]
    assert indicesOfPatternInMatrix([[2]], [[0,0,0],[0,1,0],[0,0,0]]) == []

if __name__ == "__main__":
    main()