# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        newCur = dummy
        cur1 = l1
        cur2 = l2
        leftover = 0

        while cur1 or cur2 or leftover:
            if(cur1):
                val1 = cur1.val
            else:
                val1 = 0

            if(cur2):
                val2 = cur2.val
            else:
                val2 = 0
            total = val2 + val1 + leftover

            digit = total % 10
            leftover = total // 10

            newCur.next = ListNode(digit)
            newCur = newCur.next

            if(cur1):
                cur1 = cur1.next
            if(cur2):
                cur2 = cur2.next

        return dummy.next