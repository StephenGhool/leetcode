# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Steps:
        # 1. find the kth node
        # 2. store kth.next in a temp variable
        # 3. set kth.next to None
        # 4. pass begin node into reverse function. function return head and tail
        # 5. set tail.next to temp variable
        # 6. set begin node to tail.next
        # 7. repeat step 1 to 6 
        
        #edge cases:
        if head is None:
            return head
        if k==1:
            return head
    
        
        # function would reverse the linked list passed
        def reverse_list(head):
            tail = head
            prevnode = ListNode()
            curnode = head 
            
            while(curnode):
                tmp = curnode.next
                curnode.next = prevnode
                
                prevnode = curnode
                curnode = tmp
            return prevnode, tail
        
        begin_node = head
        k_node = head
        prevnode = ListNode()
        
        while(k_node):
            for i in range(1,k):
                k_node = k_node.next if k_node else None
      
            if k_node is not None:
                tmp = k_node.next
                k_node.next = None
         
                rev_head, rev_tail = reverse_list(begin_node)
            
                if head==rev_tail:
                    head = rev_head
                else:
                    prevnode.next = rev_head
                    
                rev_tail.next = tmp
                k_node = tmp
                begin_node = tmp
                prevnode = rev_tail         
                
        return head
                