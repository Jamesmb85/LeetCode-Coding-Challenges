# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# Example:

# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

# Follow up:

# If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle

# Explanation:
# Simple idea of the Kadane’s algorithm is to look for all positive contiguous segments of the array 
# (max_ending_here is used for this). And keep track of maximum sum contiguous segment among all positive segments 
# (max_so_far is used for this). Each time we get a positive sum compare it with max_so_far and update max_so_far if 
# it is greater than max_so_far

def maximumSubArrayNumber(input_list):
        """
        :type nums: List[int]
        :rtype: int
        """

        max_value_so_far = -2147483647 #smallest int possible
        max_ending = 0

        #let's loop through the list
        for number in range(0, len(input_list)):
            max_ending += input_list[number]

            #check to see if max_value_so_far is less than the max_ending
            if(max_value_so_far < max_ending):
                max_value_so_far = max_ending

            #check to see if max_ending is less than 0, if it is, then assign 0
            if(max_ending < 0):
                max_ending = 0

        return max_value_so_far

print(maximumSubArrayNumber([-2, -3, 4, -1, -2, 1, 5, -3]))	
    # Lets take the example:
    # {-2, -3, 4, -1, -2, 1, 5, -3}

    # max_value_so_far = max_ending = 0

    # for i=0,  a[0] =  -2
    # max_ending = max_ending + (-2)
    # Set max_ending = 0 because max_ending < 0

    # for i=1,  a[1] =  -3
    # max_ending = max_ending + (-3)
    # Set max_ending = 0 because max_ending < 0

    # for i=2,  a[2] =  4
    # max_ending = max_ending + (4)
    # max_ending = 4
    # max_value_so_far is updated to 4 because max_ending greater 
    # than max_value_so_far which was 0 till now

    # for i=3,  a[3] =  -1
    # max_ending = max_ending + (-1)
    # max_ending = 3

    # for i=4,  a[4] =  -2
    # max_ending = max_ending + (-2)
    # max_ending = 1

    # for i=5,  a[5] =  1
    # max_ending = max_ending + (1)
    # max_ending = 2

    # for i=6,  a[6] =  5
    # max_ending = max_ending + (5)
    # max_ending = 7
    # max_value_so_far is updated to 7 because max_ending is 
    # greater than max_value_so_far

    # for i=7,  a[7] =  -3
    # max_ending = max_ending + (-3)
    # max_ending = 4

	
print(maximumSubArrayNumber([-2,1,-3,4,-1,2,1,-5,4]))
print(maximumSubArrayNumber([-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7] ))