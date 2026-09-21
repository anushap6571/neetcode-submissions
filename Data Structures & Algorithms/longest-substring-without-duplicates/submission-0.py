class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = {}
        maxLen = 0
        l = 0
        r = 0

        while r < len(s):
            if s[r] in hashmap and l <= hashmap[s[r]] < r:
                l = hashmap[s[r]] + 1
            hashmap[s[r]] = r
            maxLen = max(maxLen, r-l+1)
            r+=1
        return maxLen