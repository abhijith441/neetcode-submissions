class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pivot = -1
        n = len(nums)

        # find the breakpoint
        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                pivot = i
                break
        if pivot == -1:
            return nums.reverse()
        # swap the next larger element with pivot
        for i in range(n-1, pivot, -1):
            if nums[i] > nums[pivot]:
                nums[i], nums[pivot] = nums[pivot], nums[i]
                break
        # reverse the rest of the list
        nums[pivot+1:] = reversed(nums[pivot+1:])
        