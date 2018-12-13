# Given two arrays, write a function to compute their intersection.

# Example 1:

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]

# Example 2:

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]

# Note:

    # Each element in the result must be unique.
    # The result can be in any order.

def intersection(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """

    #let's convert to a set and find the intersection of the two sets
    set1 = set(nums1)
    set2 = set(nums2)
    set3 = set1.intersection(set2)

    #return as a list
    return list(set3)

print(intersection([1,2,2,1], [2,2]))
print(intersection([4,9,5], [9,4,9,8,4]))