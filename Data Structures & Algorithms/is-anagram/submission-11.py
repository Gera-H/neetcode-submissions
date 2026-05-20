class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        output = False
        s = sorted(s)
        t = sorted(t)

        if s == t:
            return not output
        else:
            return output