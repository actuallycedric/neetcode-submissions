class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            res += str(len(s))
            res += "#"
            res += s
        
        return res

    
        

    def decode(self, s: str) -> List[str]:

        i = 0

        res = []

        length = ""

        while i < len(s):
            
            while s[i] != "#":
                length += s[i]
                i += 1
            
            res.append(s[i+1:i + 1 + int(length)])

            i += int(length) + 1

            length = ""

            

        return res



