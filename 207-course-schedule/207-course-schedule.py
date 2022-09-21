class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # steps: looking for a cycle
        # 1. convert prerequisites from list array to adjacency list
        # 2. determine if there is any cycles:
        #   2.1 select node and see if it is in visited list. 
        #       2.1.1 If so return False
        #       2.1.2 If no, add node to visited list (keeps track of visited nodes)
        #   2.2 look at the neighboring nodes
        #       2.2.1 if they exist repeat step 2.1 to 2.2
        #       2.2.2 If no neighbors remove node from visited list
        #   2.4
        
        # list to keep track of visited nodes
        visited = set()
        
        # adjacency list
        nodes = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            nodes[course].append(prereq)
       
        def cycle(course):
            if course in visited:
                return False
            
            if nodes[course]==[]:
                return True
            
            visited.add(course)
        
            for nei in nodes[course]:
                if not cycle(nei): return False
                
            visited.remove(course)
            nodes[course] = []
            return True
        
        # determine for each course if there is a cycle
        for course in range(numCourses):
            if course in nodes:
                if not cycle(course): return False
        
        return True