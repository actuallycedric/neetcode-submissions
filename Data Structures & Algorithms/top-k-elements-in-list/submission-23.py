class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq_dict = {}

        for num in nums:
            if num not in freq_dict:
                freq_dict[num] = 1
            else:
                freq_dict[num] += 1

        freq_arr = []

        for num, cnt in freq_dict.items():
            freq_arr.append([cnt, num])

        freq_arr.sort()

        res = []

        while len(res) < k:
            res.append(freq_arr.pop()[1])

        return res
        