class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashPrev = {}

        for i,n in enumerate(nums):
            dif = target - n
            if dif in hashPrev:
                return [hashPrev[dif], i]
            hashPrev[n] = i
        return index