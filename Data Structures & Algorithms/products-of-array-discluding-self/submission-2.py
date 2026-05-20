class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        count = 0
        n = len(nums)
        output = [0] * len(nums)
        for i in range(n):
            if nums[i] == 0:
                count += 1
                continue
            else:
                product *= nums[i]
        
        for i in range(n):
            if count == 0:
                output[i] = int(product / nums[i])
            elif count == 1:
                if nums[i] == 0:
                    output[i] = product
        return output
