class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hasmap={i:[] for i in range(numCourses)}
        for crs,pre in prerequisites:
            hasmap[crs].append(pre)
        visited=set()
        def dfs(crs):
            if crs in visited:
                return False
            if hasmap[crs]==[]:
                return True
            visited.add(crs)
            for pre in hasmap[crs]:
                if not dfs(pre):
                    return False

            visited.remove(crs)
            hasmap[crs]=[]
            return True
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True