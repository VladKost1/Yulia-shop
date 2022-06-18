"""
Given an array of integers, find all pairs in the array that sum up to a given target value.
In other words, given an array arr and a target value target, return all pairs a, b such that a + b = target.
Assumptions:
- input array is not sorted
- elements are unique in the input array
Example:
Input array: [7, 12, 3, 1, 2, -6, 5, -8, 6]
Target sum: 0
Output: [(-6,6)]
-6 6
Target sum: 8
Output: [(7,1), (3,5), (2, 6)]
7 1
3 5
2 6
"""


def get_pairs_sum(arr, n, res):
    count = {}
    for i in range(0, n):
        temp = res - arr[i]
        if temp in count:
            print(f'Pairs of sum {res} is ({temp}, {arr[i]})')
        count[arr[i]] = i


# Driver function
arr = [7, 12, 3, 1, 2, -6, 5, -8, 6]
n = 0
get_pairs_sum(arr, len(arr), n)
