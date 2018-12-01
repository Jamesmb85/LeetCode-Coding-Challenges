# Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

# Example 1:

# Input: 121
# Output: true

# Example 2:

# Input: -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

# Example 3:

# Input: 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

# Follow up:

# Coud you solve it without converting the integer to a string?

# Note: my Java solution to a similar problem uses a loop and removes the ones digit and appendes it to a new values
# After the look a comparison is made. The solution is found here:
# https://github.com/Jamesmb85/Java-8-Bootcamp-Challenges-Solutions/blob/master/Palindrome_Function_Challenge.java

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x  = str(x) #convert number to a string
        return x == x[::-1] #string slicing where the whole string is returned in reverse. 