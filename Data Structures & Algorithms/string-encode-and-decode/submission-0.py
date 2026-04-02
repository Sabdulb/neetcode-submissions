class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ""
        for s in strs:
            ret += str(len(s)) + "#" + s
        return ret


    def decode(self, s: str) -> List[str]:
        i = 0
        temp = ""
        ans = []
        while i < len(s):
            if s[i] != "#":
                temp += s[i]
                i += 1
            else:
                i += 1
                ans.append(s[i:i + int(temp)])
                i = i + int(temp)
                temp = ""
        return ans


        
        
        
            
