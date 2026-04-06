class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = defaultdict(list)

        for s in strs:

            freq_map = [0] * 26

            for c in s:
                char_index = ord(c) - ord('a')

                freq_map[char_index] += 1

            res[tuple(freq_map)].append(s)

        return list(res.values())
        