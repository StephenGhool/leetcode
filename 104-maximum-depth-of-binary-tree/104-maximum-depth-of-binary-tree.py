# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # steps (using dfs to find longest path)
        # 1. start at the root node
        # 2. Does node have neighbors?
        #   2.1 yes 
        #       2.1.1 add neighors to stack
        #       2.1.2 goto left neighbor and increment count, remove node from stack
        #       2.1.3 repeat step2
        #   2.2 no 
        #       2.2.1 if stack empty:
        #           2.2.1.1 no - goto next node in stack
        #           2.2.1.2 yes - goto step3
        #       2.2.2 repeat step2
        
        
        depth = 0

        def dfs(node, depth):
            if node is not None:
                return max(dfs(node.left,depth+1), dfs(node.right,depth+1))
            else:
                return depth
            
        
        return dfs(root, depth)
