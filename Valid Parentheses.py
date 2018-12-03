# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

    # Open brackets must be closed by the same type of brackets.
    # Open brackets must be closed in the correct order.

# Note that an empty string is also considered valid.

# Example 1:

# Input: "()"
# Output: true

# Example 2:

# Input: "()[]{}"
# Output: true

# Example 3:

# Input: "(]"
# Output: false

# Example 4:

# Input: "([)]"
# Output: false

# Example 5:

# Input: "{[]}"
# Output: true



def isValid(s):
    """
    :type s: str
    :rtype: bool
    """

    #need to iterate through the string and check if all of the characters are an open or close bracket
    #we also need to check if the matching open/close bracket exist

    #let's use a stack so we can add and remove brackets as we find them
    #list in python are used to implement stacks
    workingStack = []

    #let's traverse through the string and look for opening brackets
    for value in s:
        #check to see if value is an opening bracket, if it is, then push to the stack
        if(value == "(" or value == "{" or value == "["):
            workingStack.append(value)
        #check to see if one of the closing brackets exist, the stack is empty and there is a matching opening bracket
        elif(value == ")" and len(workingStack) != 0 and "(" in workingStack):
            #pop off the stack
            workingStack.pop()
            #check to see if one of the closing brackets exist, the stack is empty and there is a matching opening bracket
        elif(value == "}" and len(workingStack) != 0 and "{" in workingStack):
            #pop off the stack
            workingStack.pop()
            #check to see if one of the closing brackets exist, the stack is empty and there is a matching opening bracket
        elif(value == "]" and len(workingStack) != 0 and "[" in workingStack):
            #pop off the stack
            workingStack.pop()

    #after the loop, if it is empty, then we have a balanced bracket
    return workingStack == []



print(isValid("()"))
print(isValid("()[]{}"))
print(isValid("(]"))
print(isValid("([)]"))
print(isValid("{[]}"))