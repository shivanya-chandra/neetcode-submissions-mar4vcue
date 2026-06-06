# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if(not head):
            return []
        c = 1
        cur = head
        while(cur.next):
            c+=1
            cur= cur.next

        removeNode = c-n
        h = 0
        # print(c)
        if(c == 1 and n == 1):
            head =None
            return head
        # print(removeNode, "he")
        cur = head
        # print(head.val, "g")
        if((removeNode - 1) ==-1 and cur.next):
            # print("hello22")
            head = cur.next
        
        while(cur and cur.next):
            if(h ==(removeNode-1)):
                # print("yp")
                cur.next = cur.next.next
    
            cur = cur.next
            h+=1
            # print(cur.val, "hello")
        return head
