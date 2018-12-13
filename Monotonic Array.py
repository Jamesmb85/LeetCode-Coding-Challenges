# An array is monotonic if it is either monotone increasing or monotone decreasing.

# An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array A is monotone decreasing if for all i <= j, A[i] >= A[j].

# Return true if and only if the given array A is monotonic.

 

# Example 1:

# Input: [1,2,2,3]
# Output: true

# Example 2:

# Input: [6,5,4,4]
# Output: true

# Example 3:

# Input: [1,3,2]
# Output: false

# Example 4:

# Input: [1,2,4,5]
# Output: true

# Example 5:

# Input: [1,1,1]
# Output: true

 

# Note:

    # 1 <= A.length <= 50000
    # -100000 <= A[i] <= 100000



def isMonotonic(A):
    """
    :type A: List[int]
    :rtype: bool
    """

    return A == sorted(A) or A == sorted(A, reverse=True)

    # below was my logic before my solution above. It did not handle [1,1,0]
    #
    # #let's check the first two values and that will determine if the subsequent values should be higher or lower
    # if(len(A) >= 2):
    #     firstValue = A[0]
    #     secondValue = A[1]
    #
    #     if(firstValue <= secondValue):
    #         for value in range(0, len(A)-1):
    #             if(A[value] <= A[value+1]):
    #              continue
    #             #at some point is not monotonic so we return False
    #             else:
    #                 return False
    #         #we get to the end of the list and is monotonic so we return True
    #         return True
    #     elif(firstValue >= secondValue):
    #         for value in range(0, len(A)-1):
    #             if(A[value] >= A[value+1]):
    #                 continue
    #                 #at some point is not monotonic so we return False
    #             else:
    #                 return False
    #         #we get to the end of the list and is monotonic so we return True
    #         return True
    # else:
    #     #array size is less than 2, so we return True since by definition an array of size 1 is monotonic
    #     return True



print(isMonotonic([1,2,2,3]))
print(isMonotonic([6,5,4,4]))
print(isMonotonic([1,3,2]))
print(isMonotonic([1,2,4,5]))
print(isMonotonic([1,1,1]))
print(isMonotonic([1,1,0]))
print(isMonotonic([1]))