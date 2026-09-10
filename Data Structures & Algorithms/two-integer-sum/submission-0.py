class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hashmap {value: index}
        # loop through list more, subtract each value by target, 
        # and check if that exists and is not the same index
        map = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in map:
                return [map[diff], i]
            map[n] = i