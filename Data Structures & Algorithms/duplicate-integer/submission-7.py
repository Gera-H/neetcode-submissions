class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ori = len(nums)
        setO = set(nums)

        # if ori != len(setO):
        #     return True
        # else:
        #     return False

        return ori != len(setO)