class Solution:
    def checkDivisibility(self, n: int) -> bool:
        a = 0
        b = 1
        d = n
        while d > 0:
            c = d%10
            a += c
            b *= c
            d = d//10

        if n%(a+b) == 0:
            return True
        
        else: return False