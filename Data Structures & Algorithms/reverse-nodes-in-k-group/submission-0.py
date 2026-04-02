# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        

        arr = []

        temp = head

        i = 0
        while temp:
            start = temp
            count = 1
            while temp:
                if count == k:
                    save = temp.next
                    temp.next = None
                    temp = save
                    arr.append([start, True])
                    break
                if temp.next == None and count < k:
                    arr.append([start, False])
                count += 1
                temp = temp.next


        def reverse(node) -> Optional[ListNode]:
            cur = node
            prev = None

            while cur:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
            return prev

        for i in range(len(arr)):
            if arr[i][1] == True:
                arr[i][0] = reverse(arr[i][0])
        
        temp = ListNode()
        dummy = temp
        i = 0
        while dummy:
            if dummy.next == None:
                if i >= len(arr):
                    return temp.next
                dummy.next = arr[i][0]
                i += 1
            dummy = dummy.next
        
        return temp.next


