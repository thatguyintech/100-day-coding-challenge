def permutations(arr):
    allPermutations = list()

    if len(arr) <= 1:
        return [arr]
    else:
        for i in xrange(len(arr)):
            for permutation in permutations(arr[1:]):
                # when i is 0, arr[0:1] is at the beginning of this list
                allPermutations.append(permutation[:i] + arr[0:1] + permutation[i:])

    return sorted(allPermutations)

def main():
    assert permutations([1]) == [[1]]
    assert permutations([1,2]) == [[1, 2], [2, 1]]
    assert permutations([1,2,3]) == [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

if __name__ == "__main__":
    main()
