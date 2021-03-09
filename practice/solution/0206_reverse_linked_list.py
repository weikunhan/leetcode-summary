# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        dummy_head = ListNode(-1)
        dummy_head.next = head
        temp_res = dummy_head
        l1 = dummy_head.next
        l2 = None
        
        while l1:
            temp = l1.next
            l1.next = l2
            l2 = l1
            l1 = temp
            
        temp_res.next = l2
        
        return dummy_head.next