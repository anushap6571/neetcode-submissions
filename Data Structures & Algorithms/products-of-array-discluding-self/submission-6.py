class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # simple solution using the divide in O(n)
        total_product = nums[0]
        has_zero = 0
        if total_product == 0:
            has_zero += 1
            total_product = 1
        output = []
        
        i = 1
        while i < len(nums):
            if nums[i] == 0:
                has_zero += 1
            else:
                total_product *= nums[i]
            i+=1

        print(has_zero)
        print(total_product)
        for i, num in enumerate(nums):
            if has_zero == 1:
                if num == 0:
                    output.append(total_product)
                else:
                    output.append(0)
            elif has_zero > 1:
                output.append(0)
            else:
                output.append(total_product // num)

        return output
        