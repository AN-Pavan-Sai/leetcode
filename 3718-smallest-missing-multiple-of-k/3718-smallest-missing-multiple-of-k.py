class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        l = 1
        n = k

        while n in nums:
            l += 1
            n = l*k

        return n