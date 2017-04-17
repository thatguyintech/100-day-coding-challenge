
# given an array arr of integers, return a pair of indices such
# that the values in the array at those indices sum up to s
# return nothing if no sum is possible
def twoSum(arr, s):
    if len(arr) <= 0:
        return

    haveSeen = {}

    for i, num in enumerate(arr):
        if s-num in haveSeen:
            return (i, haveSeen[s-num])
        else:
            haveSeen[num] = i

    return

def isPair(indices, goalSum, arr):
    first, second = indices
    return arr[first] + arr[second] == goalSum

def tests():
    arr0 = [1, 1, 1, 1, 1]
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [1, 4, 3, 5, 2]
    arr3 = [-1, -4, -3, -5, -2]
    arr4 = []
    arr5 = [1]

    assert(isPair(twoSum(arr0, 2), 2, arr0))
    assert(isPair(twoSum(arr1, 6), 6, arr1))
    assert(twoSum(arr1, 10) == None)
    assert(twoSum(arr1, 1) == None)
    assert(twoSum(arr3, 5) == None)
    assert(isPair(twoSum(arr3, -5), -5, arr3))
    assert(twoSum(arr4, 1) == None)
    assert(twoSum(arr5, 1) == None)

tests() 