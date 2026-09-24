class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            a = nums[i]
            b = 0
            while a > 0:
                b = b + a%10
                a = a//10
            
            if b == i:
                return i
        
        else:
            return -1