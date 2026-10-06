class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        DP = [[False] * n for _ in range(n)]
        besti = 0
        bestLen = 0

        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or DP[i+1][j-1]):
                    DP[i][j] = True
                    if bestLen < (j-i +1):
                        besti = i
                        bestLen = j - i + 1
        return s[besti: besti+bestLen]


        