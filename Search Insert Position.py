# Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You may assume no duplicates in the array.

# Example 1:

# Input: [1,3,5,6], 5
# Output: 2

# Example 2:

# Input: [1,3,5,6], 2
# Output: 1

# Example 3:

# Input: [1,3,5,6], 7
# Output: 4

# Example 4:

# Input: [1,3,5,6], 0
# Output: 0



def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """

    #need to find the first integer that is greater than or equal to the target. That's our insertion point
    for index, value in enumerate(nums):
        if(value >= target):
            return index
        else:
            continue

    #if we get to the end of the loop and still haven't found the insertion point, we insert at the end
    return len(nums)



print(searchInsert([1,3,5,6], 5))
print(searchInsert([1,3,5,6], 2))
print(searchInsert([1,3,5,6], 7))
print(searchInsert([1,3,5,6], 0))