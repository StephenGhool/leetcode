"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # steps:
        # 1. start at node 1 and create a copy of the node
        # 2. determine the neighbors of the node
        # 3. iterate over the neighbors and determine if a node needs to be created
        #   3.1 for each neighbor repeat steps 2
        #   3.2 create neighbor node if it doesnt exist
        #   3.3 repeat steps 3 for the new neighbor nodes until no new neighbors are found
        
        # used to keep track of new and old nodes
        hashmap = {}
        def clone(node):
            # base case - node already exists - return node
            if node in hashmap:
                return hashmap[node]
            
            # create new node - new to create new node instance
            new_node = Node(node.val)
            hashmap[node] = new_node
            
            # iterate over the neighbors to connect them
            for nxt in node.neighbors:
                # append neighbors but check to see if they are created or not first then                   # append
                new_node.neighbors.append(clone(nxt))
                
            return new_node
        
        return clone(node) if node else None