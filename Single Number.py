# Given a non-empty array of integers, every element appears twice except for one. Find that single one.

# Note:

# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

# Example 1:

# Input: [2,2,1]
# Output: 1

# Example 2:

# Input: [4,1,2,1,2]
# Output: 4



def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    #let's use the count method for list. If the count of the element is one, return it and stop the loop
    #will return the first single count
    for value in nums:
        if(nums.count(value) == 1):
            return value

    return None #return None if no element has a single count


print(singleNumber([2,2,1]))
print(singleNumber([4,1,2,1,2]))
print(singleNumber([1,1,1,1,1,1,1,1,2,3,3,3,4]))
print(singleNumber([2,2,2,3,3,3]))
