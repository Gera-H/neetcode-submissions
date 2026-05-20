class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        sub = set()
        res = 0
        p = 0
        for i in range(n):
            while(s[i] in sub):
                sub.remove(s[p])
                p+=1
            sub.add(s[i])
            res = max(res, len(sub))
        return res