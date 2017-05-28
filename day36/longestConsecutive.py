def longestConsecutive(nums):
    if len(nums) <= 1:
        return len(nums)

    buckets = [False for i in xrange(max(nums)+1)]
    for num in nums:
        buckets[num] = True
    if len(buckets) == 1:
        return 1

    maxLongestCount, longestCount = 0, 1
    for prev, curr in zip(buckets, buckets[1:]):
        if prev and curr:
            longestCount += 1
        else:
            longestCount = 1
        maxLongestCount = max(maxLongestCount, longestCount)

    return maxLongestCount

def testLongestConsecutive():
    assert longestConsecutive([100, 4, 200, 1, 3, 2]) == 4
    assert longestConsecutive([]) == 0
    assert longestConsecutive([0]) == 1
    assert longestConsecutive([0, 0]) == 1 # assume duplicates don't count
    assert longestConsecutive([0, 1, 2]) == 3
    assert longestConsecutive([2, 1, 0]) == 3
    assert longestConsecutive([1, 50, 2, 51, 3, 52, 4, 53, 54]) == 5

def main():
    testLongestConsecutive()

if __name__ == "__main__":
    main()
