# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

# Note:

    # The number of elements initialized in nums1 and nums2 are m and n respectively.
    # You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.

# Example:

# Input:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3

# Output: [1,2,2,3,5,6]

# I ignored the in-place modification 

def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: void Do not return anything, modify nums1 in-place instead.
    """

    workingList = []

    #let's just use two loops and fill in the array. We can sort afterwards before returning the array
    for value in range(m):
        workingList.append(nums1[value])

    for value in range(n):
        workingList.append(nums2[value])

    return sorted(workingList)

print(merge([1,2,3,0,0,0], 3, [2,5,6], 3))