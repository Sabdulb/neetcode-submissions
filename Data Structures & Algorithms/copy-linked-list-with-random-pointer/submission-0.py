"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        temp = head
        mp = {None: None}
        while temp:
            mp[temp] = Node(temp.val)
            temp = temp.next

        prev = head
        while prev:
            mp[prev].next = mp[prev.next]
            mp[prev].random = mp[prev.random]
            prev = prev.next
        
        return mp[head]
