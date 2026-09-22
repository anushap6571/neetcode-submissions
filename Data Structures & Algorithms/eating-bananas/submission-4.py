class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math
        left = 1
        right = max(piles)
        result = right
        while left <= right:
            mid = (right+left) // 2

            # mid is the possible option
            hours = 0
            for pile in piles:
                hours += math.ceil(float(pile)/mid)

            if hours > h:
                # we undershot the amount, use second half
                left = mid + 1
            if hours <= h:
                # we overshot the amount, use first half
                result = mid
                right = mid -1
        return result

        




        