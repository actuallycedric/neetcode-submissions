class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        

        l = 0
        r = len(numbers) - 1

        while l < r:

            total = numbers[l] + numbers[r]

            if total > target: # if total is larger, decrement r (move to smaller or equal number)
                r -= 1

            elif total < target: # if total is smaller, increment l (move to bigger or equal number)
                l += 1

            else:
                return [l + 1, r + 1] # 1-indexed

        return []