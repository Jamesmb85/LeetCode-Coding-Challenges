# Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

# If the last word does not exist, return 0.

# Note: A word is defined as a character sequence consists of non-space characters only.

# Example:

# Input: "Hello World"
# Output: 5



def lengthOfLastWord(s):
    """
    :type s: str
    :rtype: int
    """

    #call the split method and return the last value in the list that is returned
    #also call the strip method to remove any whitespace. this account for an empty string
	# strip() in-built function of Python is used to remove all the leading and trailing spaces from a string.
	# remove (optional): Character or a set of characters, that needs to be removed from the string.
	# The function can take one or no parameter. If no parameter is passed then only the leading and trailing spaces are removed. 
    split_phase = s.strip(" ").split(" ")

    return len(split_phase[-1])

print(lengthOfLastWord("Hello World"))