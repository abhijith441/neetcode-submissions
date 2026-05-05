class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hmap = {}

        for i in range(len(nums)):
            value = target - nums[i]
            if value in hmap:
                return [hmap[value], i]
            hmap[nums[i]] = i
        
        