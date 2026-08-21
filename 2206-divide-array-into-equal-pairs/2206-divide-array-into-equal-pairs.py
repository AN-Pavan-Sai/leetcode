class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        n = len(nums)
        d = {}

        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

        for j in d.values():
            if j%2 != 0:
                return False
        
        return True