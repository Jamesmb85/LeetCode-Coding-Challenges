# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

# Note: For the purpose of this problem, we define empty string as valid palindrome.

# Example 1:

# Input: "A man, a plan, a canal: Panama"
# Output: true

# Example 2:

# Input: "race a car"
# Output: false



def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    workingString = []

    for character in s:
	 # isalnum() :- This function returns true when all the characters in the string are 
	 # combination of numbers and/or alphabets else returns false.
        if(character.isalnum()):
            workingString.append(character.lower())

    return workingString == workingString[::-1]

    # workingArray = []
    #
    # #lets remove all trailing and leading spaces and make everything lowercase
    # newString = s.lower().strip()
    #
    # #let's iterate over the string and put alphanumeric character in an array
    # for character in newString:
    #     workingArray.append(character)
    #
    # counter = 0
    #
    # #let's iterate through the array backwards and the  string forward and compare characters
    # for value in reversed(s):
    #     if(value == workingArray[counter]):
    #         counter = counter + 1
    #         continue
    #     else:
    #         return False
    #
    # #if we make it through the loop, then all of the characters in the reversed string and array match
    # return True



print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome("race a car"))
print(isPalindrome("mom"))
print(isPalindrome("Mom"))