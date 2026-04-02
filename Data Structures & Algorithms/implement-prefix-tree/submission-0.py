class PrefixTree:

    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        temp = self.trie

        for i in range(len(word)):

            if word[i] not in temp:
                temp[word[i]] = {}
            temp = temp[word[i]]
            if i == len(word) - 1:
                temp["end"] = True

    def search(self, word: str) -> bool:
        temp = self.trie

        for i in range(len(word)):
            if word[i] not in temp:
                return False
            temp = temp[word[i]]
            if i == len(word) - 1:
                return temp.get("end", False)

    def startsWith(self, prefix: str) -> bool:
        temp = self.trie

        for i in range(len(prefix)):
            if prefix[i] not in temp:
                return False
            temp = temp[prefix[i]]
        
        return True
        
        