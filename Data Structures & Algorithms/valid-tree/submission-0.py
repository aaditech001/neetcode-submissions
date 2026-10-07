class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        graph = {i: [] for i in range(n)}
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited=set()
        visited.add(0)

        def dfs(node,parent):
            for neighbour in graph[node]:
                if neighbour==parent:
                    continue
                if neighbour in visited:
                    return False
                visited.add(neighbour)

                if not dfs(neighbour, node):
                    return False
            return True

        if not dfs(0, -1):
            return False
            

        return len(visited)==n
        