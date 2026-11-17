class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        s_dict = defaultdict(list)

        for s in strs:

            freq = [0] * 26

            for ch in s:
                ch_idx = ord(ch) - ord('a')

                freq[ch_idx] += 1
            
            s_dict[tuple(freq)].append(s)

        return list(s_dict.values())
            
