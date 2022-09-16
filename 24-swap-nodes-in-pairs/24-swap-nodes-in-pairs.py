# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # steps:
        # 1. create empty head -> dummy node
        # 2. check if there are at least two nodes
        # 3. update node 1 to point to the next of node 2
        # 4. update node 2 to point to next of dummy node
        # 5. update dummy node to point at node 2
        # 6. update all pointers
        
        # initailize
        node1 = head
        node2 = node1.next if head else None
        
        dummy = ListNode()
        dummy.next = node1
        
        cnt = 0
        
        while(node1):
            # check if node 2 exists
            if node2 is not None:
                node1.next = node2.next
                node2.next = dummy.next
                dummy.next = node2
                
               
                # update head (the head only updates once)
                if cnt <1:
                    head = dummy.next
                cnt+=1
                print(dummy)
                
            # update node pointers
            dummy = node1
            node1 = node1.next if node1 else None
            node2 = node1.next if node1 else None
            
        return head

        
        
                
        
        
        
        