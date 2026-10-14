class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = x**n
        low = -2**31
        high = (2**31)+1
        if ans < low  :
            return low
        if ans > high:
            return high
        return x**n
