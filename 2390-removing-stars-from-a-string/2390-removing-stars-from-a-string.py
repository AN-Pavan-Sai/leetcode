class Solution:
    def removeStars(self, s: str) -> str:
        a = ""
        for i in range(len(s)):
            if s[i] == "*":
                a = a[:-1]
            else:
                a += s[i]

        return a