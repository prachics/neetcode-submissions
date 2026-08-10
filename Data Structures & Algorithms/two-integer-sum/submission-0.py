class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            tofind = target - nums[i]
            if tofind in seen:
                return [seen[tofind],i]
            else:
                seen[nums[i]] = i


