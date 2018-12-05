# Merge two sorted linked lists and return it as a new list. 
# The new list should be made by splicing together the nodes of the first two lists.

# Example:

# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        #create a temp node Null
        temp = None
        
        #if l1 or l2 is empty then return the other list
        if(l1 is None):
            return l2
        if(l2 is None):
            return l1
        
        # If List1's data is smaller or 
        # equal to List2's data
        if(l1.val <=l2.val):
            # assign temp to List1's data 
            temp = l1 

            # Again check List1's data is smaller or equal List2's  
            # data and call mergeTwoLists function. 
            temp.next = self.mergeTwoLists(l1.next, l2)
            
        else:
            # If List2's data is greater than or equal List1's  
            # data assign temp to l2 
            temp = l2
            
            # Again check List1's data is smaller or equal List2's  
            # data and call mergeTwoLists function. 
            temp.next = self.mergeTwoLists(l1, l2.next)
            
        # return the temp list. 
        return temp 
            
        
