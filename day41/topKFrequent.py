def topKFrequent(nums, k):

    return ret

def testTopKFrequent():
    assert set(topKFrequent([], 0)) == set([])
    assert set(topKFrequent([1], 1)) == set([1])
    assert set(topKFrequent([-1, -1], 1)) == set([-1])
    assert set(topKFrequent([1,1,1,2,2,3], 2)) == set([1, 2])
    assert set(topKFrequent([-1,-1,-1,2,2,3], 2)) == set([-1, 2])
    assert set(topKFrequent([1,1,1,2,2,3], 3)) == set([1, 2, 3])
    assert set(topKFrequent([1,1,1,2,2,2,3,3,3], 3)) == set([1, 2, 3])
    assert set(topKFrequent([1, 2, 3, 4, 5], 1)) == set([1, 2, 3, 4, 5])
    assert set(topKFrequent([4,1,-1,2,-1,2,3], 2)) == set([-1, 2])
    assert set(topKFrequent([3,2,3,1,2,4,5,5,6,7,7,8,2,3,1,1,1,10,11,5,6,2,4,7,8,5,6], 10)) == set([1,2,5,3,7,6,4,8,10,11])

def main():
    testTopKFrequent()

if __name__ == "__main__":
    main()
