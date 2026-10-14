class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        ans= ""
        while sum>9:
            ans+="9"
            sum-=9
        ans+=str(sum)
        if len(ans)>num:
            return ""
        else:
            return ans + "0"*(num-len(ans))

        
