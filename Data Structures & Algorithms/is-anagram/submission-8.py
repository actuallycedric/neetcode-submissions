class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        freq = {}

        for c in s:
            
            freq[c] = 1 + freq.get(c, 0)

        for c in t:
            freq[c] = -1 + freq.get(c, 0)

        for v in freq.values():
            if v != 0:
                return False
        
        return True
        