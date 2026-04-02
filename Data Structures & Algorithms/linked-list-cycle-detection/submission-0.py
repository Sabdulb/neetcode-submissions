# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        mp = {}
        while head:
            if head in mp:
                return True
            else:
                mp[head] = 1
                head = head.next
        return False