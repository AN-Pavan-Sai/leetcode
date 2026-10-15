class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        result = []
        ans = 0
        for i in range(n):
            sub = []
            for j in range(i, n):
                sub.append(nums[j])
                result.append(sub.copy())

        for i in result:
            ans += len(set(i))**2

        return ans
