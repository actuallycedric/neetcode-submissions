class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = defaultdict(list)

        for s in strs:

            freq = [0] * 26

            for ch in s:
                ch_idx = ord(ch) - 97

                freq[ch_idx] += 1

            res[tuple(freq)].append(s)
        
        return list(res.values())

            
        