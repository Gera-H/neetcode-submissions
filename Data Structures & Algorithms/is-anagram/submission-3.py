class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for i in s:
                if s.count(i) != t.count(i):
                    return False
        if len(s) == len(t):
            return True
        return False