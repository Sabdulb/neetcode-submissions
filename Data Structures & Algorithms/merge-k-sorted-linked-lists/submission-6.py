# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if len(lists) == 0:
            return None
        
        ans = lists[0]



        def merge(head1, head2):

            dummy = ListNode()
            tail = dummy

            while head1 or head2:
                if head1 and head2:
                    if head1.val <= head2.val:
                        tail.next = head1
                        tail = tail.next
                        head1 = head1.next
                    else:
                        print(head2.val)
                        tail.next = head2
                        tail = tail.next
                        head2 = head2.next
                elif head1:
                    tail.next = head1
                    tail = tail.next
                    head1 = head1.next
                else:
                    tail.next = head2
                    tail = tail.next
                    head2 = head2.next
            
            return dummy.next
        

        for i in range(1, len(lists), 1):
            ans = merge(ans, lists[i])
        
        return ans