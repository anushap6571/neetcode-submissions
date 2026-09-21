class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        result = []

        for i, a in enumerate(nums):
            if a > 0:
                break
            if i > 0 and a == nums[i-1]:
                continue # keep moving through duplicates of a bc they're already accounted for
            l = i+1
            r = len(nums) - 1

            while l < r:
                threesum = a + nums[l] + nums[r]
                if threesum > 0:
                    # move the right pointer down
                    r-=1
                elif threesum < 0:
                    # move the left pointer up
                    l += 1
                else:
                    result.append([a, nums[l], nums[r]])
                    l+=1
                    r-=1
                    while nums[l] == nums[l-1] and l < r:
                        l+=1 # skip through duplicates for b and c
        return result
