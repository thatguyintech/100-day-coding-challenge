def topKFrequent(nums, k):
    if len(nums) == 0:
        return []

    freqs = dict()
    for num in nums:
        if num in freqs:
            freqs[num] += 1
        else:
            freqs[num] = 1

    buckets = [None for i in xrange(max(freqs.keys())+1)]

    for num in freqs:
        freq = freqs[num]
        if buckets[freq]:
            buckets[freq].append(num)
        else:
            buckets[freq] = [num]

    ret = []
    i = len(buckets)-1
    addedCount = 0
    offset = 0
    while addedCount < k:
        while not buckets[i-offset-addedCount]:
            offset += 1
        ret += buckets[i-offset-addedCount]
        addedCount += 1

    return ret

def testTopKFrequent():
    assert set(topKFrequent([], 0)) == set([])
    assert set(topKFrequent([1], 1)) == set([1])
    assert set(topKFrequent([1,1,1,2,2,3], 2)) == set([1, 2])
    assert set(topKFrequent([-1,-1,-1,2,2,3], 2)) == set([-1, 2])
    assert set(topKFrequent([1,1,1,2,2,3], 3)) == set([1, 2, 3])
    assert set(topKFrequent([1, 2, 3, 4, 5], 1)) == set([1, 2, 3, 4, 5])

def main():
    testTopKFrequent()

if __name__ == "__main__":
    main()
