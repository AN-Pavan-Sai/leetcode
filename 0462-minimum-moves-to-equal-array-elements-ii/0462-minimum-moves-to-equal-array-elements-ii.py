class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        d = nums[len(nums)//2]
        count = 0
        for i in range(len(nums)):
            count += abs(d-nums[i])

        return count