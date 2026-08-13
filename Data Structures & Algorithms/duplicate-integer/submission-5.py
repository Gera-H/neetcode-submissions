class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setD = set();
        for n in nums:
            if n in setD:
                return True
            setD.add(n)
        return False