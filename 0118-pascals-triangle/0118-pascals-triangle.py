import math

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        n = numRows
        if n==1:
            return [[1]]
        arr = [[1],[1,1]]

        for i in range(2,n):
            row = []

            for j in range(i + 1):
                value = math.factorial(i) // (
                    math.factorial(j) * math.factorial(i - j)
                )

                row.append(value)

            arr.append(row)

        return arr

