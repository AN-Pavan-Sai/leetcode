class Solution:
    def minMoves(self, nums: List[int]) -> int:
        c = max(nums)
        count = 0

        for i in range(len(nums)):
            count += c-nums[i]

        return count