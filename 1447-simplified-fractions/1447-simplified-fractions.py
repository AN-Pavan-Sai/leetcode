import math

class Solution:
    def simplifiedFractions(self, n: int) -> list[str]:
        lst = []

        for i in range(1,n):
            for j in range(2,n+1):
                if math.gcd(i,j) == 1 and i < j:
                    lst.append(str(i)+"/"+str(j))

        return lst