class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        mp = defaultdict(set)
        visit = set()
        q = deque()

        for word in wordList:
            for i in range(len(word)):
                temp = word[:i] + "*" + word[i + 1:]
                mp[temp].add(word)
        

        def bfs(word):
            if word in visit:
                return False
            
            if word == endWord:
                return True
            
            visit.add(word)
            q.append(word)

            return False
        dist = 1
        q.append(beginWord)

        while q:
            for i in range(len(q)):
                word = q.popleft()
                for j in range(len(word)):
                    temp = word[:j] + "*" + word[j + 1:]
                    for c in mp[temp]:
                        if bfs(c):
                            return dist + 1
            dist += 1
        
        return 0
                


