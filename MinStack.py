 # Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

    # push(x) -- Push element x onto stack.
    # pop() -- Removes the element on top of the stack.
    # top() -- Get the top element.
    # getMin() -- Retrieve the minimum element in the stack.

# Example:

# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> Returns -3.
# minStack.pop();
# minStack.top();      --> Returns 0.
# minStack.getMin();   --> Returns -2.



class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
		#list is the DS we are going to use for the MinStack class
        self.workingList = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
		#since we are using lists, we can use the append method
        self.workingList.append(x)
        

    def pop(self):
        """
        :rtype: void
        """
		#since we are using lists, we can use the pop method
        self.workingList.pop()
        

    def top(self):
        """
        :rtype: int
        """
		#since we are using lists, we can use reverse index to start at the back of the list.
        return self.workingList[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return min(self.workingList)
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()