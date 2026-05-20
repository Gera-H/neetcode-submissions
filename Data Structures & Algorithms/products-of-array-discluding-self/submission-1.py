class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        overPro = 1
        countZ = 0
        for i in nums:
            if i != 0:
                overPro *= i
            else:
                countZ +=1
        
        result = []
        for i in range(len(nums)):
            if countZ >=2:
                result.append(0)
            elif countZ ==1:
                if nums[i] == 0:
                    result.append(int(overPro))
                else:
                    result.append(0)
            else:
                result.append(int(overPro/nums[i]))
        return result