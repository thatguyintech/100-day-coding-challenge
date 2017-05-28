def reverseStr(s, k):
    # edge
    size = len(s)
    if size < k:
        return s[::-1]

    # convert string to list
    letters = list(s)
    i = 0

    # reverse all the full chunks
    while i + 2*k-1 < size:
        reverse(letters, i, i+k-1)
        i += 2*k

    # take care of the remainder
    if i+k-1 < size:
        reverse(letters, i, i+k-1)
    else:
        reverse(letters, i, size-1)

    # fin
    return "".join(letters)

# reverses the indices of arr between start and end, in place
def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def testReverse():
    t1 = [0, 1, 2, 3, 4]
    reverse(t1, 0, 2)
    assert t1 == [2, 1, 0, 3, 4]

    t2 = [0, 1, 2, 3, 4]
    reverse(t2, 1, 3)
    assert t2 == [0, 3, 2, 1, 4]

def testReverseStr():
    assert reverseStr("", 1) == ""
    assert reverseStr("", 2) == ""
    assert reverseStr("", 10000) == ""
    assert reverseStr("abcdefg", 1) == "abcdefg"
    assert reverseStr("abcdefg", 2) == "bacdfeg"
    assert reverseStr("abcdefg", 3) == "cbadefg"
    assert reverseStr("abcdefg", 4) == "dcbaefg"
    assert reverseStr("abcdefg", 5) == "edcbafg"
    assert reverseStr("abcdefg", 6) == "fedcbag"
    assert reverseStr("abcdefg", 7) == "gfedcba"
    assert reverseStr("abcdefg", 8) == "gfedcba"
    assert reverseStr("abcdefg", 9) == "gfedcba"

def main():
    testReverse()
    testReverseStr()

if __name__ == "__main__":
    main()
