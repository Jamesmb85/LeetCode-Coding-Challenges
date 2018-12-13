# Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

# Find all the elements of [1, n] inclusive that do not appear in this array.

# Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

# Example:

# Input:
# [4,3,2,7,8,2,3,1]

# Output:
# [5,6]


def findDisappearedNumbers(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """

    workingArray = []

    #let's create an array and fill it with numbers from 1 to size of the array
    for value in range(1, len(nums)+1):
        workingArray.append(value)

   #let's convert workingArray and nums to a set so we can find the difference
    set1 = set(nums)
    set2 = set(workingArray)

    set3 = set2.difference(set1)

    return list(set3)

print(findDisappearedNumbers([4,3,2,7,8,2,3,1]))