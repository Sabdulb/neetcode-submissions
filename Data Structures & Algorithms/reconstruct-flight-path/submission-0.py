class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        tickets.sort()

        ret = ["JFK"]

        mp = defaultdict(list)

        for src,dst in tickets:

            mp[src].append(dst)

        def dfs(node):

            if len(ret) == len(tickets) + 1:
                return True
            
            if node not in mp:
                return False
            
            temp = list(mp[node])
            for i,v in enumerate(temp):
                mp[node].pop(i)
                ret.append(v)
                if dfs(v): return True
                mp[node].insert(i,v)
                ret.pop()
            
            return False
        
        dfs("JFK")
        return ret

