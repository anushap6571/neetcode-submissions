class Solution:
    def climbStairs(self, n: int) -> int:
        
        # simple recursive is too inefficient
        # try dp instead

        DP = [1] * (n+1)
        if n <= 2:
            return n
        DP[1], DP[2] = 1, 2
        
        
        for i in range(3, n+1):
            DP[i] = DP[i-2] + DP[i-1]
        
        return DP[n]