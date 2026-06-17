class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = len(nums) - 1
        index = 0

        while index <= right:

            if nums[index] == 0:
                temp = nums[left]
                nums[left] = nums[index]
                nums[index] = temp
                index += 1
                left += 1

            elif nums[index] == 1:
                index += 1
            
            else:
                temp = nums[right]
                nums[right] = nums[index]
                nums[index] = temp
                right -= 1
        

        