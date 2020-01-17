"""This problem was asked by Google.

Given an array of integers and a number k, where 1 <= k <= length of the array, compute the maximum values of each subarray of length k.

For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:

10 = max(10, 5, 2)
7 = max(5, 2, 7)
8 = max(2, 7, 8)
8 = max(7, 8, 7)
Do this in O(n) time and O(k) space. You can modify the input array in-place and you do not need to store the results. You can simply print them out as you compute them."""
from collections import deque

def subarray_max(array, k):
    dq = deque() # while always be stricly descending (by corresponding value) and have at most k elements

    for i in range(k):
        while dq and array[i] >= array[dq[-1]]:
            dq.pop()
        dq.append(i)
    yield array[dq[0]]

    for i in range(k, len(array)):
        if dq[0] == i-k:
            dq.popleft()

        while dq and array[i] >= array[dq[-1]]:
            dq.pop()
        dq.append(i)
        yield array[dq[0]]


def test_subarray_max():
    assert list(subarray_max(array=[10, 5, 2, 7, 8, 7], k=3)) == [10, 7, 8, 8]
    assert list(subarray_max(array=[7, 8, 7, 2, 5, 10], k=3)) == [8, 8, 7, 10]
    assert list(subarray_max(array=[10, 5, 2, 7, 8, 7], k=1)) == [10, 5, 2, 7, 8, 7]
    assert list(subarray_max(array=[10, 5, 2, 7, 8, 7], k=5)) == [10, 8]
