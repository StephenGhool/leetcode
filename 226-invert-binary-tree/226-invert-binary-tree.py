# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # steps
        # 1. traverse the tree until the node.next is none
        # 2. move to next node in stack
        # 3. check if node.next is None
        #   3.1 Yes
        #       3.1.1 goto step 2
        #   3.2 No
        #       3.2.1 flip the child nodes
        #       3.2.2 goto step1
        
        # edge cases
        if root is None:
            return root
        
        if root.left is None and root.right is None:
            return root
        
        # invert node children
        left_child = root.left
        root.left = root.right
        root.right =left_child
        
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root
        