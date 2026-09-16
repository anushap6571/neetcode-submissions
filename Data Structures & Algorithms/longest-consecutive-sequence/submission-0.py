class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        max_len = 0
        hashset = set(nums)

        for num in hashset:

            if num-1 not in hashset:
                length = 1
                while (num + length) in hashset:
                    length += 1
                max_len = max(length, max_len)
        

        return max_len
                

