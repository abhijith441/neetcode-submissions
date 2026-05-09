class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # calculate left product for every element
        # calculate right product for every element
        # multiply everythig together

        # left product
        prefix = 1

        result = [1 for num in nums]
        prefix = 1
        postfix = 1

        for i in range(len(nums)):
            result [i] = prefix
            prefix = prefix * nums[i]
        
        for j in range(len(nums)-1, -1, -1):
            result[j] = result[j] * postfix
            postfix = postfix * nums[j]
        

        
        print (result)

        return result
            





        