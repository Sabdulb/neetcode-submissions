class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        ret = []

        mp = {
            2: ["a","b","c"],
            3: ["d","e","f"],
            4: ["g","h","i"],
            5: ["j","k","l"],
            6: ["m","n","o"],
            7: ["p","q","r","s"],
            8: ["t","u","v"],
            9: ["w","x","y","z"]
        }

        def dfs(i, cur):

            if i >= len(digits):
                ret.append(cur)
                return
            
            for val in mp[int(digits[i])]:
                temp = cur
                temp += val
                dfs(i + 1, temp)
        
        dfs(0, "")

        if len(digits) == 0:
            return []
        else:
            return ret
