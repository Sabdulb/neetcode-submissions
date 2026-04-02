# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow,fast = head,head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        fast = slow.next
        slow.next = None
        slow = head

        curr = fast
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        fast = prev

        while fast:
            temp = slow.next
            slow.next = fast
            temp2 = fast.next
            fast.next = temp
            fast = temp2
            slow = temp


        
        
        

