class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        found = set()
        mp = defaultdict(list)

        for i,j in prerequisites:
            mp[i].append(j)
        
        for i in range(numCourses):
            if i not in mp:
                found.add(i)
        
        def dfs(i, visit):

            if i in visit:
                return False
            
            if i in found:
                return True
            
            visit.add(i)
            for key in mp[i]:
                if dfs(key, visit) == False:
                    return False
            
            found.add(i)
            return True
        
        print(found)
        for i in range(numCourses):
            if i not in found:
                if dfs(i, set()) == False:
                    return False
        
        return True
            