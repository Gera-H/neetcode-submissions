class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            print("this is i:",i)
            for j in range(len(nums)):
                if j == i:
                    continue
                else:
                    if nums[j] == nums[i]:
                        return True
        return False