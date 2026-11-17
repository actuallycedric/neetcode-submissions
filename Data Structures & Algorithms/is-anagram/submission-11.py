class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        freq = {}

        for ch in s:
            if ch not in freq:
                freq[ch] = 1
            else:
                freq[ch] += 1
        
        for ch in t:
            if ch not in freq:
                return False
            else:
                freq[ch] -= 1

        for val in freq.values():
            if val != 0:
                return False

        return True
        