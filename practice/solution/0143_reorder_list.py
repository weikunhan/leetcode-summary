# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        
        if not head:
            
            return
        
        left = head
        right = head
       
        while right and right.next:
            right = right.next.next
            left = left.next
        
        l1 = left.next
        left.next = None
        l2 = None
        
        while l1:
            temp = l1.next
            l1.next = l2
            l2 = l1
            l1 = temp
        
        left = head
        right = l2
        
        while right:
            temp = right.next
            right.next = left.next
            left.next = right
            left = left.next.next
            right = temp
