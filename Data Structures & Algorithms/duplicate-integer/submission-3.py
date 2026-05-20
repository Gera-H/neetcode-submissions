class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicateHash = {}
        output = False

        for i in nums:
            if i in duplicateHash:
                return not output
            duplicateHash[i] = 1
        return output