# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = -1
        temp = head
        while temp:
            count += 1
            temp = temp.next
        
        curr = head

        i = 0
        if count - n < 0:
            head = head.next
            return head

        while i < (count - n):
            i += 1
            curr = curr.next
        
        curr.next = curr.next.next

        return head

