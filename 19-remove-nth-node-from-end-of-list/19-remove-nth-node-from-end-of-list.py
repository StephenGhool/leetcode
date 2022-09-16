# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Steps:
        # 1. find the (n+1)th node
        # 2. prev ptr equal to n+1 node
        # 3. post ptr equal to n - 1 node(given that it exists)
        # 4. remove nth node connection to n-1
        # 5. set prev.next equal to postnode
        
        # length of linkedlist
        link_length = self.length(head)
        
        prevnode = head
        
        # edge cases
        if link_length==0:
            return None
        
        if link_length == n:
            head = head.next
            return head
        
        for i in range(link_length - n -1):
            prevnode = prevnode.next
        
      
        postnode = prevnode.next.next
        prevnode.next.next = None
        prevnode.next = postnode
        return head
        
    def length(self,head):
        if head.next is None:
            return 1
        else:
            return 1 + self.length(head.next) 