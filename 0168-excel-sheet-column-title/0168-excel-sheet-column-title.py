class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        s = ""
        n = columnNumber

        while n > 0:
            n -= 1
            r = n%26
            s = chr((r)+65) + s
            n = n//26

        return s

        