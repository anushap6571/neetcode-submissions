class Solution:
    def rob(self, nums: List[int]) -> int:
        # the best sum at the current index is the value of the current index 
        # + the best sum at current - 2 index. 

        n = len(nums)
        if n <= 2:
            return max(nums)
        DP = [0] * n

        DP[0] = nums[0]
        DP[1] = max(nums[0], nums[1])


        for i in range(2, n):
            DP[i] = max(DP[i-1], DP[i-2] + nums[i])

        return max(DP[n-1], DP[n-2])

