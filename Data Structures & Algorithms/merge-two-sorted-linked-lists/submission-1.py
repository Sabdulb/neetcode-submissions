# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        ret = None
        ans = None

        while list1 or list2:

            if list1 and list2:
                
                if list1.val <= list2.val:
                    if ret == None:
                        ret = list1
                    else:
                        ret.next = list1
                        ret = ret.next
                    list1 = list1.next
                else:
                    if ret == None:
                        ret = list2
                    else:
                        ret.next = list2
                        ret = ret.next
                    list2 = list2.next
                if ans == None:
                    ans = ret
                continue
            
            if list1:
                if ret == None:
                    ret = list1
                else:
                    ret.next = list1
                    ret = ret.next
                list1 = list1.next
                if ans == None:
                    ans = ret
                continue
            
            if list2:
                if ret == None:
                    ret = list2
                else:
                    ret.next = list2
                    ret = ret.next
                list2 = list2.next
                if ans == None:
                    ans = ret
                continue

        return ans
            

