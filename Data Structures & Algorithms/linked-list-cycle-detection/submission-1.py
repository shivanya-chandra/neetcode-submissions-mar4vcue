# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
            a= []
            dummy = head
            cur = dummy
            if(not head):
                return False

            while (cur.next):
                if cur.val in a:
                    return True
                # print(cur.val)
                a.append(cur.val)
                # print(a)

                cur = cur.next

            return False