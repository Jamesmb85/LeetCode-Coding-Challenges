# Implement strStr().

# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# Example 1:

# Input: haystack = "hello", needle = "ll"
# Output: 2

# Example 2:

# Input: haystack = "aaaaa", needle = "bba"
# Output: -1

# Clarification:

# What should we return when needle is an empty string? This is a great question to ask during an interview.

# For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().



def strStr(self, haystack, needle):
	"""
	:type haystack: str
	:type needle: str
	:rtype: int
	"""
	# The find() method returns the lowest index of the substring if it is found in given string. If its is not found then it returns -1.
	if(haystack.find(needle) != -1):
		 return haystack.find(needle)
	else:
		 return haystack.find(needle)