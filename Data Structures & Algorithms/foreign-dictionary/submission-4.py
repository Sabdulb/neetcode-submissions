class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        
        mp = defaultdict(set)

        visit = set()
        total = set()

        for i in range(len(words)):
            for j in range(i + 1, len(words)):

                first = words[i]
                second = words[j]

                k = 0

                for k in range(min(len(first), len(second))):

                    if first[k] == second[k]:
                        if len(first) > len(second) and k == len(second) - 1:
                            return ""
                        continue
                    else:
                        mp[second[k]].add(first[k])
                        break
        ret = []
        def dfs(c):

            if c in total:
                return True

            if c not in mp:
                ret.append(c)
                total.add(c)
                return True
            
            if c in visit:
                return False
            
            visit.add(c)
            for chars in mp[c]:
                if dfs(chars) == False: return False
            visit.remove(c)

            total.add(c)
            ret.append(c)

            return True
        

        for key in mp.keys():
            if dfs(key) == False: return ""
        
        for word in words:
            for char in word:
                if char not in mp and char not in total:
                    total.add(char)
                    ret.append(char)
        
        return "".join(ret)


