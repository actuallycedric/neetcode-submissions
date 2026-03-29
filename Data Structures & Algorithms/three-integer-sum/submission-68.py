class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        

        indices = []

        nums.sort()

        for i in range(len(nums)):

            target = 0 - nums[i]

            l = i + 1
            r = len(nums) - 1

            if nums[i] > 0: break # no more further numbers can add to zero
            if i > 0 and nums[i] == nums[i-1]: continue # skip dupes

            while l < r: # 2sum w sorted array implementation
                
                total = nums[l] + nums[r]

                if total > target:
                    r -= 1

                elif total < target:
                    l += 1

                else:
                    triplet = [nums[l], nums[r], nums[i]]
                    indices.append(triplet)

                    l += 1
                    r -= 1

                    while nums[l] == nums[l - 1] and l < r: l += 1
                    

                
                
        
        return indices

