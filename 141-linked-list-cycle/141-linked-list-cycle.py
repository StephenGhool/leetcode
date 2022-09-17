# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # steps
        # 1. determine length of linked list
        # 2. check and see if pos is within the link length
        
#         if pos< 0:
#             return false
#         else:
#             return true
        # print(head.pos())
        

        
        # steps:
        # 1. iterate over the linked list
        # 2. add next value and ptrs to it in hashmap
        # 3. if the value is in hashmap return trueee else false
        
        
        # dummy node
        dummy = ListNode()
        cur = dummy
        cur.next = head 
        
        # edge cases
        if head is None or head.next is None:
            return False
        
        # hashmap to store past value locations
        hashmap = {}
        
        while(cur.next is not None):
         
            if cur.next in hashmap:
                return True
            
            hashmap[cur.next] = cur.next.val
            cur = cur.next
        return False
            