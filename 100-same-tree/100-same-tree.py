# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_stack = [p]
        q_stack = [q]
        
        while len(p_stack) > 0 or len(q_stack) > 0:
            
            p_node = p_stack.pop()
            q_node = q_stack.pop()
            
            if p_node is None and q_node is not None:
                return False
            
            if q_node is None and p_node is not None:
                return False
            
            if p_node is not None and q_node is not None:

                if p_node.val!= q_node.val:
                    return False

                q_stack.append(q_node.left)
                p_stack.append(p_node.left)
                q_stack.append(q_node.right)
                p_stack.append(p_node.right)
            
        return True