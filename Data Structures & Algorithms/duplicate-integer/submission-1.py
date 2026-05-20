class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        thisSet = set()
        for i in nums:
            if i in thisSet:
                return True
            thisSet.add(i)
            print(i)
        return False
        