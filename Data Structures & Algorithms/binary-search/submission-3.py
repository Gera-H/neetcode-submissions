class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        r = n-1
        l = 0
        
        while(l <= r):
            m = int((l+r)/2)
            if nums[m] < target:
                l = m+1
            elif nums[m] > target:
                r = m-1
            else:
                return m
        return -1