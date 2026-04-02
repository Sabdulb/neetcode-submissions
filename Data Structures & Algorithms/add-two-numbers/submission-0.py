# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        arr1 = []
        arr2 = []

        temp1 = l1
        while temp1:
            arr1.insert(0, temp1.val)
            temp1 = temp1.next
        
        temp2 = l2
        while temp2:
            arr2.insert(0, temp2.val)
            temp2 = temp2.next
        

        s1 = ""
        s2 = ""

        for val in arr1:
            s1 += str(val)
        
        for val in arr2:
            s2 += str(val)
        
        num = int(s1) + int(s2)

        ans = str(num)

        nex = None

        for i in range(len(ans)):
            curr = ListNode(int(ans[i]))
            curr.next = nex
            nex = curr
        
        return curr