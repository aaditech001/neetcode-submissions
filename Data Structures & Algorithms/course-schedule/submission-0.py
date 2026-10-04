class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)] 

        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)  
        visited = set()
        path = set()    

        def dfs(node):  
            if node in path:
                return False    
            if node in visited:
                return True 
            path.add(node)  
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False    
            path.remove(node)
            visited.add(node)   
            return True 
            
        for course in range(numCourses):
            if not dfs(course):
                return False    
        return True