class WordDictionary:

    def __init__(self):
        self.children = {}

    def addWord(self, word: str) -> None:
        temp = self.children

        for i in range(len(word)):
            temp[word[i]] = temp.get(word[i], {})
            temp = temp[word[i]]

            if i == len(word) - 1:
                temp["end"] = True

    def search(self, word: str) -> bool:

        arr = [False]

        def dfs(i, child):

            if i == len(word):
                arr[0] = arr[0] | child.get("end", False)
                return
            
            if word[i] != ".":
                child = child.get(word[i], None)
                if child is None:
                    return
                else:
                    dfs(i + 1, child)
            else:
                for key in child.keys():
                    if key != "end":
                        dfs(i + 1, child[key])
            
        dfs(0, self.children)

        return arr[0]
            


        
