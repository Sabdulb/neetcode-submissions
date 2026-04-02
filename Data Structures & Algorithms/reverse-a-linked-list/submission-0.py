# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = head
        cur = None

        # [0,1,2,3]

        while prev is not None:
            temp = prev.next 
            prev.next = cur
            cur = prev
            prev = temp
        return cur




