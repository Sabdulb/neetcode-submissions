class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        ret = []
        found = set()
        visit = set()
        mp = defaultdict(list)

        for i,j in prerequisites:
            mp[i].append(j)
        
        def dfs(course, visit):

            if course not in mp or course in found:
                if course not in found:
                    found.add(course)
                    ret.append(course)
                return True
            
            if course in visit:
                return False

            visit.add(course)
            
            for vals in mp[course]:

                if dfs(vals, visit) == False:
                    return False
                
            found.add(course)
            ret.append(course)

            return True
        
        for i in range(numCourses):
            if dfs(i, set()) == False:
                return []
        
        return ret
                
        
